# Data Science and Machine Learning in Chemical Engineering

**06-642 · Spring 2026 · Carnegie Mellon University**

Welcome to the course! This half-semester course covers practical applications of data science and machine learning techniques to problems in chemical engineering and related sciences.

## Course Goals

By the end of this course, you will be able to:

1. **Manipulate data** using NumPy and Pandas for analysis and visualization
2. **Build predictive models** using scikit-learn for regression and classification
3. **Apply advanced techniques** including ensemble methods, clustering, and dimensionality reduction
4. **Quantify uncertainty** in model predictions using pycse and Gaussian processes
5. **Interpret models** to understand what drives predictions
6. **Apply these skills** to real chemical engineering problems

## Course Structure

The course consists of 12 lectures covering:

| Module | Topic |
|--------|-------|
| 00 | Introduction & Python Environment |
| 01 | NumPy Fundamentals |
| 02 | Pandas Introduction |
| 03 | Intermediate Pandas |
| 04 | Dimensionality Reduction |
| 05 | Linear Regression |
| 06 | Regularization & Model Selection |
| 07 | Nonlinear Methods |
| 08 | Ensemble Methods |
| 09 | Clustering |
| 10 | Uncertainty Quantification |
| 11 | Model Interpretability |

Plus optional lectures on databases, deep learning, symbolic regression, and LLMs.

## Prerequisites

- Basic Python programming
- Undergraduate mathematics (linear algebra, calculus, statistics)
- No prior machine learning experience required

## Interactive Learning

This course includes an interactive learning system to help reinforce concepts:

### Data Academy Honors
Earn badges and ranks as you progress:
- **5 Badges**: Data Wrangler, Pattern Seeker, Model Builder, Ensemble Master, Uncertainty Expert
- **4 Ranks**: Data Apprentice → Data Analyst → Data Scientist → Senior Data Scientist

See [Data Academy Honors](data-academy-honors/README.md) for details.

### Games & Activities
- **Trivia** (`/trivia`): Test your knowledge with character-hosted questions
- **Adventure** (`/adventure`): "The Data Detective Agency" - solve ChemE data mysteries
- **Flashcards** (`/flashcards`): Spaced repetition for key concepts
- **Puzzles** (`/puzzle`): Metric matching, confusion matrices, code completion
- **Scavenger Hunts** (`/hunt`): Explore datasets, documentation, and papers

### Course Characters
Meet your guides including Nadia Null, Reggie Regression, Val Validation, and more! See [characters.md](characters.md).

### Quick Reference
The [reference sheet](reference-sheet.md) provides concise summaries of pandas, sklearn, metrics, and common patterns.

## Repository Setup

### Initial Setup

```bash
# Clone the course repository
git clone <course-repo-url>
cd dsmles

# Install notebook merge tool (handles Jupyter notebook conflicts)
pip install nbdime
nbdime config-git --enable --global

# Create your working branch (keep main clean for updates)
git checkout -b my-work
```

### Getting Course Updates

When the instructor announces updates:

```bash
# Switch to main and pull updates
git checkout main
git pull origin main

# Return to your working branch
git checkout my-work

# Optionally merge updates into your branch
git merge main
```

If you encounter notebook merge conflicts, nbdime provides a visual merge tool:

```bash
git mergetool --tool=nbdime
```

### Why This Workflow?

- **main branch** stays clean and always pulls without conflicts
- **your branch** contains all your work, notes, and completed exercises
- **you control** when to bring in updates
- **nbdime** handles notebook merges intelligently when needed

## Getting Started

1. Review the {doc}`syllabus` for course policies
2. Set up your Python environment (see {doc}`00-introduction/introduction`)
3. Clone the repo and create your working branch (see above)
4. Complete assignments as they are released
5. Try `/trivia` to test your knowledge as you learn!

Let's begin!
