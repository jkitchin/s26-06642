# Data Science Puzzles

Challenge yourself with interactive data science puzzles!

## Your Task

Read puzzles from `games/puzzles/puzzles.json` and run an interactive puzzle session.

### Puzzle Types

1. **Metric Match**: Match metrics to appropriate use cases
2. **Code Completion**: Fill in missing pandas/sklearn code
3. **Confusion Matrix Analysis**: Calculate metrics from matrices
4. **Algorithm Detective**: Identify algorithms from behavior

### Session Flow

1. **Puzzle Selection**:
   - Ask for puzzle type preference or random
   - Filter by completed lectures
   - Offer difficulty selection (easy/medium/hard)

2. **Puzzle Presentation**:
   - Clear instructions
   - All necessary information displayed
   - For matching: show items to match
   - For code: show template with blanks

3. **Solution Input**:
   - Accept answers in appropriate format
   - Allow multiple attempts for partial credit

4. **Feedback**:
   - Show correct answers
   - Explain the reasoning
   - Award points based on accuracy

### Points System

- Easy puzzles: 15-20 points
- Medium puzzles: 20-25 points
- Hard puzzles: 25-35 points
- Partial credit available

### Example: Confusion Matrix Puzzle

```
🧩 Confusion Matrix Challenge

Given this confusion matrix for a reactor fault detector:

              Predicted
              Safe    Fault
Actual Safe   180     10
Actual Fault  5       5

Questions:
1. What is the precision for detecting faults?
2. What is the recall for detecting faults?
3. Is this detector safe to use? Why?

Your answers:
```

### Example: Code Completion

```
🧩 Code Completion

Complete the cross-validation pipeline:

from sklearn.pipeline import ______
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import ______

pipe = ______([(
    ('scaler', StandardScaler()),
    ('model', Ridge(alpha=1.0))
])

scores = ______(pipe, X, y, cv=5)

Fill in the blanks (comma-separated):
```

Start a puzzle challenge now!
