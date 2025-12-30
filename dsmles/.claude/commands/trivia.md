# Data Science Trivia

Play a trivia game to test your data science and machine learning knowledge!

## Your Task

Read the trivia pool from `games/trivia/trivia-pool.json` and run an interactive trivia session.

### Game Rules

1. **Question Selection**: Select 5 random questions appropriate for the student's progress
   - Check which lectures have been completed (ask if unknown)
   - Only include questions from completed lectures
   - Mix difficulties: 2 easy, 2 medium, 1 hard

2. **Question Format**: For each question:
   - Show the character mascot and their icon
   - Display the question clearly
   - Show numbered options (1-4)
   - Wait for student response

3. **Feedback**:
   - Correct: Celebrate and show points earned (+10, +5 streak bonus if applicable)
   - Incorrect: Show correct answer with explanation
   - Always include the character's study tip

4. **Scoring**:
   - 10 points per correct answer
   - +5 bonus for streaks of 3+ correct
   - Track total and display at end

5. **End of Round**:
   - Show final score out of possible points
   - Highlight any weak areas (lectures with wrong answers)
   - Suggest review topics if score < 70%

### Character Integration

Each question has an associated character. Use their personality:
- **Practice Panda**: Encouraging, hands-on tips
- **Nadia Null**: Mysterious hints about missing data
- **Otto Outlier**: Wild observations about edge cases
- **Cora Correlation**: Careful warnings about causation
- **Val Validation**: Skeptical reminders about testing
- **And others...**

### Example Interaction

```
🐼 Practice Panda asks:

What NumPy function creates an array of evenly spaced values?

1. np.linspace()
2. np.arange()
3. np.zeros()
4. Both A and B

Your answer (1-4):
```

Start the trivia game now!
