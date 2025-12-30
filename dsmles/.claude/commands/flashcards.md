# Data Science Flashcards

Study data science concepts with spaced repetition flashcards!

## Your Task

Read the flashcard decks from `games/flashcards/decks.json` and run an interactive study session.

### Study Modes

1. **By Deck**: Study a specific topic deck
2. **By Lecture**: Study cards from a specific lecture
3. **Review Due**: Cards due for review (spaced repetition)
4. **Quick Quiz**: Random selection across all decks

### Session Flow

1. **Deck Selection**:
   - Show available decks with card counts
   - Let student choose or recommend based on progress

2. **Card Presentation**:
   - Show the front (question/term)
   - Wait for student to indicate ready
   - Reveal the back (answer/definition)

3. **Self-Assessment** (SM-2 inspired):
   - Again (1): Didn't know it - review soon
   - Hard (3): Got it with difficulty - review in 3 days
   - Good (5): Got it - review in 5 days
   - Easy (7): Too easy - review in 7 days

4. **Session Summary**:
   - Cards studied
   - Performance breakdown
   - Recommended next review time

### Available Decks

- NumPy Essentials
- pandas Fundamentals
- Missing Data (Nadia Null)
- Outliers (Otto Outlier)
- Correlation (Cora Correlation)
- PCA (Dee Dimension)
- t-SNE & UMAP
- Linear Regression (Reggie Regression)
- Regularization (Ridge & Lasso)
- Cross-Validation (Val Validation)
- Bias-Variance (Barry Bias-Variance)
- Random Forest (Forrest Random)
- Gradient Boosting (Greta Gradient-Boost)
- Clustering (Clara Cluster)
- Hierarchical Clustering
- Uncertainty (Quinn Quantify)
- SHAP (SHAP Shapley)
- Evaluation Metrics
- scikit-learn Patterns

### Example Interaction

```
📚 Flashcard Study Session

Deck: Regularization (Ridge & Lasso)
Card 1 of 6

─────────────────────────
FRONT:
Ridge regression penalty
─────────────────────────

[Press Enter when ready to see answer]

─────────────────────────
BACK:
L2: α × Σβ² (shrinks coefficients toward zero)
─────────────────────────

How well did you know this?
1 - Again (didn't know)
2 - Hard (struggled)
3 - Good (knew it)
4 - Easy (too easy)

Your rating (1-4):
```

Start your flashcard session now!
