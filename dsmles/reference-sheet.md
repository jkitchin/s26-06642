# Data Science Quick Reference Sheet

A concise reference for key concepts, formulas, and code patterns.

---

## 1. Data Manipulation (pandas)

### Loading Data
```python
df = pd.read_csv('file.csv')
df = pd.read_excel('file.xlsx')
df = pd.read_json('file.json')
```

### Basic Inspection
```python
df.head(n)          # First n rows
df.tail(n)          # Last n rows
df.info()           # Data types, non-null counts
df.describe()       # Statistical summary
df.shape            # (rows, columns)
df.columns          # Column names
df.dtypes           # Column data types
```

### Selection
```python
df['col']                    # Single column (Series)
df[['col1', 'col2']]         # Multiple columns (DataFrame)
df.loc[row_label, col_label] # By label
df.iloc[row_idx, col_idx]    # By integer position
df.query('col > 5')          # Query string
```

### Missing Data (Nadia Null)
```python
df.isna().sum()              # Count missing per column
df.dropna()                  # Drop rows with any missing
df.dropna(subset=['col'])    # Drop if specific col missing
df.fillna(value)             # Fill with value
df.fillna(df.mean())         # Fill with column means
df.interpolate()             # Interpolate missing values
```

### GroupBy Operations
```python
df.groupby('col').mean()
df.groupby(['col1', 'col2']).agg({'col3': 'sum', 'col4': 'mean'})
df.pivot_table(values='y', index='a', columns='b', aggfunc='mean')
```

---

## 2. Visualization (Viz Vizzy)

### Matplotlib Basics
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='data')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.legend()
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
plt.show()
```

### Common Plot Types
```python
# Scatter
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)

# Histogram
plt.hist(data, bins=30, edgecolor='black')

# Box plot
df.boxplot(column='y', by='category')

# Heatmap (seaborn)
import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
```

### Seaborn Shortcuts
```python
sns.pairplot(df)                    # Pairwise relationships
sns.heatmap(df.corr())              # Correlation heatmap
sns.boxplot(x='cat', y='num', data=df)  # Box by category
sns.histplot(df['col'], kde=True)   # Histogram with KDE
```

---

## 3. Evaluation Metrics

### Regression
| Metric | Formula | Use When |
|--------|---------|----------|
| **MSE** | $\frac{1}{n}\sum(y - \hat{y})^2$ | Penalize large errors |
| **RMSE** | $\sqrt{MSE}$ | Same units as target |
| **MAE** | $\frac{1}{n}\sum|y - \hat{y}|$ | Robust to outliers |
| **R²** | $1 - \frac{SS_{res}}{SS_{tot}}$ | Variance explained |
| **Adjusted R²** | Penalized for # features | Model comparison |

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mse = mean_squared_error(y_true, y_pred)
rmse = mean_squared_error(y_true, y_pred, squared=False)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
```

### Classification
| Metric | Formula | Use When |
|--------|---------|----------|
| **Accuracy** | $\frac{TP + TN}{Total}$ | Balanced classes |
| **Precision** | $\frac{TP}{TP + FP}$ | Minimize false positives |
| **Recall** | $\frac{TP}{TP + FN}$ | Minimize false negatives |
| **F1 Score** | $2 \times \frac{P \times R}{P + R}$ | Balance P and R |
| **AUC-ROC** | Area under ROC | Overall ranking |

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
```

---

## 4. scikit-learn Patterns

### Basic Workflow
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit on train only!
X_test_scaled = scaler.transform(X_test)        # transform test

# Model
model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
```

### Pipeline (Prevents Data Leakage!)
```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
```

### Cross-Validation
```python
from sklearn.model_selection import cross_val_score, KFold

# Simple CV
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"R² = {scores.mean():.3f} ± {scores.std():.3f}")

# Custom CV
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold)
```

### Grid Search
```python
from sklearn.model_selection import GridSearchCV

param_grid = {'alpha': [0.01, 0.1, 1, 10, 100]}

grid = GridSearchCV(Ridge(), param_grid, cv=5, scoring='r2')
grid.fit(X_train, y_train)

print(f"Best alpha: {grid.best_params_}")
print(f"Best score: {grid.best_score_:.3f}")
```

---

## 5. Linear Models

### Linear Regression (Reggie Regression)
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

# Coefficients
print(model.coef_)       # Feature weights
print(model.intercept_)  # Bias term
```

### Regularization (Ridge & Lasso)
```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet

# Ridge (L2) - shrinks all coefficients
ridge = Ridge(alpha=1.0)

# Lasso (L1) - can zero out coefficients
lasso = Lasso(alpha=0.1)

# ElasticNet (L1 + L2)
enet = ElasticNet(alpha=0.1, l1_ratio=0.5)
```

| Method | Penalty | Effect | Use When |
|--------|---------|--------|----------|
| **Ridge** | $\alpha \sum \beta_j^2$ | Shrinks all | Multicollinearity |
| **Lasso** | $\alpha \sum |\beta_j|$ | Sparsity | Feature selection |
| **ElasticNet** | Both | Mix | Many correlated features |

---

## 6. Ensemble Methods

### Random Forest (Forrest Random)
```python
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

rf = RandomForestRegressor(
    n_estimators=100,      # Number of trees
    max_depth=10,          # Tree depth limit
    min_samples_split=5,   # Min samples to split
    random_state=42
)
rf.fit(X_train, y_train)

# Feature importance
importance = pd.Series(rf.feature_importances_, index=X.columns)
importance.sort_values().plot(kind='barh')
```

### Gradient Boosting (Greta Gradient-Boost)
```python
from sklearn.ensemble import GradientBoostingRegressor
# Or use XGBoost:
from xgboost import XGBRegressor

xgb = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,     # Lower = more trees needed
    max_depth=5,
    random_state=42
)
xgb.fit(X_train, y_train)
```

---

## 7. Dimensionality Reduction (Dee Dimension)

### PCA
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Always scale first!
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=0.95)  # Keep 95% variance
X_pca = pca.fit_transform(X_scaled)

# Analysis
print(f"Components: {pca.n_components_}")
print(f"Explained variance: {pca.explained_variance_ratio_}")

# Scree plot
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
```

### t-SNE (for visualization only)
```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels)
```

---

## 8. Clustering (Clara Cluster)

### K-Means
```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# Elbow method
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.plot(range(1, 11), inertias, 'bo-')
plt.xlabel('k')
plt.ylabel('Inertia')
```

### DBSCAN (arbitrary shapes, outlier detection)
```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)
# labels == -1 means noise/outlier
```

### Evaluation
```python
from sklearn.metrics import silhouette_score

score = silhouette_score(X_scaled, labels)  # -1 to 1, higher better
```

---

## 9. Uncertainty Quantification (Quinn Quantify)

### Bootstrap Confidence Interval
```python
from sklearn.utils import resample

n_boot = 1000
predictions = []

for _ in range(n_boot):
    X_boot, y_boot = resample(X_train, y_train)
    model.fit(X_boot, y_boot)
    predictions.append(model.predict(X_test))

predictions = np.array(predictions)
ci_low = np.percentile(predictions, 2.5, axis=0)
ci_high = np.percentile(predictions, 97.5, axis=0)
```

### Ensemble Uncertainty
```python
# For Random Forest
predictions = np.array([tree.predict(X_test) for tree in rf.estimators_])
mean_pred = predictions.mean(axis=0)
std_pred = predictions.std(axis=0)
```

---

## 10. Model Interpretability (SHAP Shapley)

### SHAP Values
```python
import shap

# For tree models
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Summary plot (global)
shap.summary_plot(shap_values, X_test)

# Single prediction (local)
shap.force_plot(explainer.expected_value, shap_values[0], X_test.iloc[0])

# Dependence plot
shap.dependence_plot('feature_name', shap_values, X_test)
```

---

## 11. Common Pitfalls (Val Validation)

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Data Leakage** | Test info in training | Split first, then preprocess |
| **Scaling before split** | Leaks test statistics | fit_transform on train only |
| **Not shuffling** | Temporal bias | Use shuffle=True (unless time series) |
| **Evaluating on train** | Overly optimistic | Always use held-out test set |
| **Ignoring class imbalance** | Poor minority class | Use stratified splits, class weights |
| **Too many features** | Overfitting | Regularization, feature selection |
| **Ignoring outliers** | Skewed results | Investigate before removing |

---

## 12. Quick Decision Guide

**Regression or Classification?**
- Continuous target → Regression
- Categorical target → Classification

**Which regression model?**
- Start with Linear Regression (baseline)
- Many features → Lasso or Ridge
- Nonlinear → Polynomial features, Random Forest, XGBoost

**Which classification model?**
- Start with Logistic Regression (baseline)
- Complex boundaries → Random Forest, XGBoost
- Need probabilities → Logistic, Random Forest

**How many clusters?**
- Use elbow method (inertia)
- Silhouette score
- Domain knowledge!

---

*"Plot it first, validate always, and never trust a model you can't explain."*
