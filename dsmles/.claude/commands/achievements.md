# Data Academy Honors - Progress Tracker

View your progress toward badges and ranks!

## Your Task

Read progress from `data-academy-honors/tracking.json` and display achievement status.

### Information to Display

1. **Current Rank**: Display current rank with icon

2. **Badge Progress**:
   For each of the 5 badges:
   - 🔍 Data Wrangler (Lectures 01-03)
   - 🗜️ Pattern Seeker (Lecture 04)
   - 🎯 Model Builder (Lectures 05-07)
   - 🌲 Ensemble Master (Lectures 08-09)
   - 📏 Uncertainty Expert (Lectures 10-11)

   Show for each:
   - Quiz average vs. required 75%
   - Assignments completed
   - Badge activity status
   - Overall progress %

3. **Next Steps**:
   - What's needed to earn next badge
   - What's needed for next rank
   - Suggested activities

4. **Game Stats** (if available):
   - Trivia high scores
   - Adventure chapters completed
   - Flashcard review status
   - Scavenger hunts finished

### Display Format

```
═══════════════════════════════════════════
     DATA ACADEMY HONORS PROGRESS
═══════════════════════════════════════════

Current Rank: 📊 Data Analyst
Badges Earned: 2 of 5

─────────────────────────────────────────────
BADGE PROGRESS
─────────────────────────────────────────────

🔍 Data Wrangler          ████████████ EARNED
   Quizzes: 82% | Assignments: 3/3 | Activity: ✓

🗜️ Pattern Seeker         ████████████ EARNED
   Quizzes: 78% | Assignments: 1/1 | Activity: ✓

🎯 Model Builder          ████████░░░░ 75%
   Quizzes: 76% | Assignments: 2/3 | Activity: pending

🌲 Ensemble Master        ░░░░░░░░░░░░ 0%
   Lectures not yet completed

📏 Uncertainty Expert     ░░░░░░░░░░░░ 0%
   Lectures not yet completed

─────────────────────────────────────────────
NEXT STEPS
─────────────────────────────────────────────

To earn Model Builder badge:
• Complete assignment for lecture 07
• Choose and complete a badge activity:
  - Property Prediction project
  - Regularization Study
  - Cross-Validation Demo

To reach Data Scientist rank:
• Earn 2 more badges
• Complete a field experience
• Submit modeling project capstone

─────────────────────────────────────────────
GAME STATISTICS
─────────────────────────────────────────────

Trivia:        Best: 45/50 | Games: 8
Adventure:     Chapters: 3/8 | Points: 850
Flashcards:    Cards studied: 127 | Due: 15
Scavenger:     Hunts: 2/11 | Points: 95

═══════════════════════════════════════════
```

### Commands

- `/achievements` - Show full progress
- `/achievements badges` - Badge details only
- `/achievements ranks` - Rank requirements only
- `/achievements next` - Next steps only

Show the student's progress now!
