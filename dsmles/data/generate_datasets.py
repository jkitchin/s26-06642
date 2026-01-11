"""
Generate all pre-generated datasets for the course notebooks.
Run this script once to create all CSV files that notebooks will load.
All datasets use seed=42 for reproducibility.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
import os

# Ensure we're in the data directory
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def save_csv(df, filename):
    """Save DataFrame to CSV in the data directory."""
    path = os.path.join(DATA_DIR, filename)
    df.to_csv(path, index=False)
    print(f"Created: {filename} ({len(df)} rows)")

# ==============================================================================
# 01-numpy: reactor_data.csv, catalyst_experiments.txt
# ==============================================================================
print("\n=== 01-numpy ===")

reactor_data = pd.DataFrame({
    'temperature': [350, 375, 400, 425, 450, 475, 500],
    'pressure': [1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5],
    'flow_rate': [2.5, 2.8, 3.0, 3.2, 3.5, 3.8, 4.0],
    'conversion': [45.2, 52.1, 61.8, 68.4, 74.9, 79.3, 83.7]
})
save_csv(reactor_data, 'reactor_data.csv')

catalyst_experiments = pd.DataFrame({
    'catalyst_id': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1'],
    'temperature': [350.0, 375.0, 400.0, 425.0, 450.0, 475.0, 500.0],
    'pressure': [1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.5],
    'yield': [45.2, 52.1, 61.8, 68.4, 74.9, 79.3, 83.7],
    'selectivity': [78.5, 81.3, 85.2, 87.9, 89.1, 90.4, 91.8]
})
save_csv(catalyst_experiments, 'catalyst_experiments.csv')

# ==============================================================================
# 03-intermediate-pandas: experiments data
# ==============================================================================
print("\n=== 03-intermediate-pandas ===")

np.random.seed(42)
n = 50
experiments_intermediate = pd.DataFrame({
    'experiment_id': [f'EXP{i:03d}' for i in range(1, n+1)],
    'date': pd.date_range('2024-01-01', periods=n, freq='D'),
    'catalyst': np.random.choice(['Pt/Al2O3', 'Pd/Al2O3', 'Ru/Al2O3'], n),
    'temperature': np.random.choice([300, 350, 400, 450, 500], n),
    'pressure': np.round(np.random.uniform(1, 5, n), 1),
    'conversion': np.round(np.random.uniform(0.3, 0.95, n), 3),
    'selectivity': np.round(np.random.uniform(0.7, 0.98, n), 3)
})
experiments_intermediate['yield'] = np.round(
    experiments_intermediate['conversion'] * experiments_intermediate['selectivity'] * 100, 1
)
save_csv(experiments_intermediate, 'experiments_intermediate.csv')

catalyst_info = pd.DataFrame({
    'catalyst': ['Pt/Al2O3', 'Pd/Al2O3', 'Ru/Al2O3', 'Rh/Al2O3'],
    'metal_loading': [1.0, 0.5, 2.0, 0.3],
    'surface_area': [250, 280, 220, 300],
    'cost_per_kg': [50000, 30000, 8000, 80000]
})
save_csv(catalyst_info, 'catalyst_info.csv')

# ==============================================================================
# 04-feature-engineering: kinetics and feature selection data
# ==============================================================================
print("\n=== 04-feature-engineering ===")

np.random.seed(42)
# Kinetics data
A, Ea, R_gas, n_order = 1e8, 50000, 8.314, 1.5
T = np.random.uniform(300, 400, 100)
C = np.random.uniform(0.1, 2.0, 100)
k = A * np.exp(-Ea / (R_gas * T))
rate_true = k * C**n_order
rate_observed = rate_true * np.exp(np.random.normal(0, 0.1, 100))

kinetics_data = pd.DataFrame({
    'temperature': T,
    'concentration': C,
    'rate': rate_observed
})
save_csv(kinetics_data, 'kinetics_data.csv')

# Feature selection data
np.random.seed(42)
n_samples = 200
X1 = np.random.uniform(0, 10, n_samples)
X2 = np.random.uniform(0, 5, n_samples)
X3 = np.random.uniform(0, 1, n_samples)
X_noise = np.random.randn(n_samples, 7)
y = 3*X1 + 1.5*X2 + 0.5*X3 + np.random.randn(n_samples)*2

feature_selection_data = pd.DataFrame({
    'X1_strong': X1,
    'X2_moderate': X2,
    'X3_weak': X3,
    'noise_0': X_noise[:, 0],
    'noise_1': X_noise[:, 1],
    'noise_2': X_noise[:, 2],
    'noise_3': X_noise[:, 3],
    'noise_4': X_noise[:, 4],
    'noise_5': X_noise[:, 5],
    'noise_6': X_noise[:, 6],
    'y': y
})
save_csv(feature_selection_data, 'feature_selection_data.csv')

# ==============================================================================
# 05-dimensionality-reduction: catalyst characterization
# ==============================================================================
print("\n=== 05-dimensionality-reduction ===")

np.random.seed(42)
n_samples = 200

# Base properties for each catalyst type
base_props = {
    'Type_A': [100, 50, 0.8, 300, 25, 1.2, 0.05, 2.5],
    'Type_B': [150, 30, 0.5, 250, 35, 0.8, 0.08, 3.0],
    'Type_C': [80, 70, 0.9, 350, 20, 1.5, 0.03, 2.0]
}
feature_names = ['surface_area', 'pore_volume', 'acidity', 'crystallite_size',
                 'metal_dispersion', 'reduction_temp', 'impurity_level', 'particle_size']

catalyst_types = np.random.choice(['Type_A', 'Type_B', 'Type_C'], n_samples)
data = []
for cat_type in catalyst_types:
    base = base_props[cat_type]
    row = [b * (1 + np.random.normal(0, 0.1)) for b in base]
    row.append(cat_type)
    data.append(row)

catalyst_char = pd.DataFrame(data, columns=feature_names + ['catalyst_type'])
save_csv(catalyst_char, 'catalyst_characterization.csv')

# ==============================================================================
# 06-linear-regression: reactor experiment
# ==============================================================================
print("\n=== 06-linear-regression ===")

np.random.seed(42)
n = 100
temperature = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 10, n)
catalyst_loading = np.random.uniform(0.5, 5, n)
residence_time = np.random.uniform(1, 30, n)

conversion = (
    0.1 * (temperature - 300) / 200 +
    0.05 * pressure +
    0.08 * catalyst_loading +
    0.01 * residence_time +
    np.random.normal(0, 0.05, n)
)
conversion = np.clip(conversion, 0, 1)

linear_regression_data = pd.DataFrame({
    'temperature': temperature,
    'pressure': pressure,
    'catalyst_loading': catalyst_loading,
    'residence_time': residence_time,
    'conversion': conversion
})
save_csv(linear_regression_data, 'linear_regression_data.csv')

# ==============================================================================
# 07-classification: quality control, multiclass, imbalanced
# ==============================================================================
print("\n=== 07-classification ===")

# Quality control data
np.random.seed(42)
n_samples = 300

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

temp_dev = np.random.normal(0, 2, n_samples)
pressure_dev = np.random.normal(0, 1.5, n_samples)
impurity = np.random.exponential(0.5, n_samples)

quality_score = -0.3*np.abs(temp_dev) - 0.4*np.abs(pressure_dev) - 1.5*impurity + 1
quality_prob = sigmoid(quality_score * 2)
quality = (np.random.random(n_samples) < quality_prob).astype(int)

quality_control = pd.DataFrame({
    'temp_deviation': temp_dev,
    'pressure_deviation': pressure_dev,
    'impurity_level': impurity,
    'quality': quality
})
save_csv(quality_control, 'quality_control.csv')

# Multi-class regime data
X_multi, y_multi = make_classification(
    n_samples=500, n_features=4, n_informative=3, n_redundant=1,
    n_classes=4, n_clusters_per_class=1, random_state=42
)
multiclass_data = pd.DataFrame(X_multi, columns=['feature_1', 'feature_2', 'feature_3', 'feature_4'])
multiclass_data['regime'] = y_multi
save_csv(multiclass_data, 'multiclass_regime.csv')

# Imbalanced fault detection
X_imb, y_imb = make_classification(
    n_samples=1000, n_features=4, n_informative=3, n_redundant=1,
    n_classes=2, weights=[0.9, 0.1], random_state=42
)
imbalanced_data = pd.DataFrame(X_imb, columns=['feature_1', 'feature_2', 'feature_3', 'feature_4'])
imbalanced_data['fault'] = y_imb
save_csv(imbalanced_data, 'imbalanced_fault.csv')

# ==============================================================================
# 08-regularization: sparse regression
# ==============================================================================
print("\n=== 08-regularization ===")

np.random.seed(42)
n_samples, n_features = 100, 50
X = np.random.randn(n_samples, n_features)
true_coef = np.zeros(n_features)
true_coef[0] = 2.0
true_coef[1] = -1.5
true_coef[2] = 1.0
true_coef[3] = 0.5
true_coef[4] = -0.8
y = X @ true_coef + np.random.normal(0, 0.5, n_samples)

sparse_data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(n_features)])
sparse_data['target'] = y
save_csv(sparse_data, 'sparse_regression.csv')

# Also save true coefficients for reference
coef_df = pd.DataFrame({'feature': [f'feature_{i}' for i in range(n_features)], 'true_coef': true_coef})
save_csv(coef_df, 'sparse_regression_true_coef.csv')

# ==============================================================================
# 09-nonlinear-methods: enzyme kinetics and reaction yield
# ==============================================================================
print("\n=== 09-nonlinear-methods ===")

# Enzyme kinetics
np.random.seed(42)
S = np.linspace(0.1, 10, 100)
Vmax, Km = 100, 2
V = Vmax * S / (Km + S) + np.random.normal(0, 3, len(S))

enzyme_kinetics = pd.DataFrame({'substrate': S, 'rate': V})
save_csv(enzyme_kinetics, 'enzyme_kinetics.csv')

# Reaction yield (2D nonlinear)
np.random.seed(42)
n = 200
temperature = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 10, n)
yield_rate = (
    0.1 * np.exp(-3000 / temperature) +
    0.05 * np.log(pressure) +
    0.001 * temperature * pressure / 100 +
    np.random.normal(0, 0.02, n)
)

reaction_yield = pd.DataFrame({
    'temperature': temperature,
    'pressure': pressure,
    'yield': yield_rate
})
save_csv(reaction_yield, 'reaction_yield.csv')

# ==============================================================================
# 10-ensemble-methods: catalyst process
# ==============================================================================
print("\n=== 10-ensemble-methods ===")

np.random.seed(42)
n = 500
temperature = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 20, n)
catalyst_loading = np.random.uniform(0.1, 5, n)
residence_time = np.random.uniform(1, 60, n)
feed_ratio = np.random.uniform(0.5, 3, n)
impurity_level = np.random.uniform(0, 0.1, n)

# Complex nonlinear conversion model
conversion = (
    0.3 * (1 - np.exp(-0.01 * (temperature - 300))) *  # Arrhenius-like
    (1 - np.exp(-0.1 * pressure)) *                     # Pressure effect
    np.tanh(0.5 * catalyst_loading) *                   # Catalyst saturation
    (1 - np.exp(-0.05 * residence_time)) *             # Time effect
    np.exp(-feed_ratio / 3) *                           # Feed ratio
    (1 - 5 * impurity_level) +                          # Impurity inhibition
    np.random.normal(0, 0.02, n)
)
conversion = np.clip(conversion, 0, 1)

ensemble_data = pd.DataFrame({
    'temperature': temperature,
    'pressure': pressure,
    'catalyst_loading': catalyst_loading,
    'residence_time': residence_time,
    'feed_ratio': feed_ratio,
    'impurity_level': impurity_level,
    'conversion': conversion
})
save_csv(ensemble_data, 'ensemble_process.csv')

# ==============================================================================
# 11-clustering: material properties
# ==============================================================================
print("\n=== 11-clustering ===")

np.random.seed(42)
n_per_type = 50

# Three polymer types with different properties
type1 = np.column_stack([
    np.random.normal(100, 10, n_per_type),   # tensile_strength
    np.random.normal(20, 5, n_per_type),     # elongation
    np.random.normal(3.5, 0.3, n_per_type),  # density
    np.random.normal(150, 15, n_per_type),   # melting_point
    np.random.normal(80, 10, n_per_type)     # hardness
])

type2 = np.column_stack([
    np.random.normal(30, 8, n_per_type),     # rubber-like
    np.random.normal(300, 50, n_per_type),
    np.random.normal(1.2, 0.1, n_per_type),
    np.random.normal(80, 10, n_per_type),
    np.random.normal(40, 8, n_per_type)
])

type3 = np.column_stack([
    np.random.normal(60, 12, n_per_type),    # medium properties
    np.random.normal(100, 20, n_per_type),
    np.random.normal(2.0, 0.2, n_per_type),
    np.random.normal(120, 12, n_per_type),
    np.random.normal(60, 10, n_per_type)
])

X_cluster = np.vstack([type1, type2, type3])
true_labels = np.array([0]*n_per_type + [1]*n_per_type + [2]*n_per_type)

clustering_data = pd.DataFrame(X_cluster, columns=[
    'tensile_strength', 'elongation', 'density', 'melting_point', 'hardness'
])
clustering_data['true_label'] = true_labels
save_csv(clustering_data, 'material_properties.csv')

# ==============================================================================
# 12-uncertainty-quantification: various small datasets
# ==============================================================================
print("\n=== 12-uncertainty-quantification ===")

# Arrhenius data
np.random.seed(42)
T_arr = np.array([300, 320, 340, 360, 380, 400, 420, 440])
R_gas = 8.314
Ea_true, A_true = 50000, 1e8
ln_k_true = np.log(A_true) - Ea_true / (R_gas * T_arr)
ln_k = ln_k_true + np.random.normal(0, 0.3, len(T_arr))

arrhenius_data = pd.DataFrame({
    'temperature': T_arr,
    'ln_k': ln_k
})
save_csv(arrhenius_data, 'arrhenius_data.csv')

# Michaelis-Menten data
np.random.seed(42)
S_mm = np.array([0.5, 1, 2, 4, 8, 16, 32, 64])
Vmax, Km = 100, 5
V_true = Vmax * S_mm / (Km + S_mm)
V_mm = V_true + np.random.normal(0, 3, len(S_mm))

michaelis_menten_data = pd.DataFrame({
    'substrate': S_mm,
    'rate': V_mm
})
save_csv(michaelis_menten_data, 'michaelis_menten.csv')

# GP training data
np.random.seed(42)
X_gp = np.array([1, 2, 3, 5, 6, 8])
y_gp = np.sin(X_gp) + np.random.normal(0, 0.1, len(X_gp))

gp_training = pd.DataFrame({'x': X_gp, 'y': y_gp})
save_csv(gp_training, 'gp_training.csv')

# Catalyst activity data
catalyst_activity = pd.DataFrame({
    'temperature': [300, 350, 400, 500, 550],
    'activity': [10, 35, 75, 95, 85]
})
save_csv(catalyst_activity, 'catalyst_activity.csv')

# ==============================================================================
# 13-model-interpretability: reactor yield
# ==============================================================================
print("\n=== 13-model-interpretability ===")

np.random.seed(42)
n = 500
temperature = np.random.uniform(300, 500, n)
pressure = np.random.uniform(1, 20, n)
catalyst_loading = np.random.uniform(0.5, 5, n)
residence_time = np.random.uniform(5, 60, n)
feed_purity = np.random.uniform(0.9, 1.0, n)
stirrer_speed = np.random.uniform(100, 500, n)

yield_product = (
    40 * (1 - np.exp(-0.01 * (temperature - 300))) *
    (1 - np.exp(-0.1 * pressure)) *
    np.tanh(0.5 * catalyst_loading) *
    (1 - np.exp(-0.05 * residence_time)) *
    feed_purity *
    (1 + 0.001 * (stirrer_speed - 300)) +
    np.random.normal(0, 2, n)
)
yield_product = np.clip(yield_product, 0, 100)

interpretability_data = pd.DataFrame({
    'temperature': temperature,
    'pressure': pressure,
    'catalyst_loading': catalyst_loading,
    'residence_time': residence_time,
    'feed_purity': feed_purity,
    'stirrer_speed': stirrer_speed,
    'yield': yield_product
})
save_csv(interpretability_data, 'interpretability_data.csv')

print("\n=== All datasets generated! ===")
