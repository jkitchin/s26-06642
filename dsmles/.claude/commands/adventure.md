# Data Detective Agency Adventure

Embark on a choose-your-own-adventure mystery using data science skills!

## Your Task

Read the adventure chapters from `games/adventure/chapters.json` and run an interactive story session.

### How It Works

1. **Chapter Selection**:
   - Check student's progress and completed lectures
   - Offer chapters that match their current knowledge
   - Allow continuing from saved progress or starting new

2. **Story Presentation**:
   - Read the chapter's narrative in an engaging way
   - Set the scene with the mystery context
   - Introduce characters naturally

3. **Decision Points**:
   - Present choices clearly with option letters (A, B, C, D)
   - Each choice represents a data science approach
   - Wait for student's decision

4. **Feedback**:
   - Optimal choice: Full points + explanation of why this approach is best
   - Good choice: Partial points + what was right and what could be better
   - Poor choice: Minimal points + learning moment about the mistake

5. **Scoring**:
   - Track points within chapter
   - Award bonus for completing chapters
   - Running total across the adventure

### Story Tone

- **Playful**: Light-hearted detective mystery
- **Educational**: Each choice teaches a real data science concept
- **ChemE-focused**: Cases involve chemical engineering scenarios
- **Brief**: 3-5 minutes per chapter reading

### Character Integration

The adventure features course characters:
- **Professor Pipeline**: Agency director, gives case briefings
- **Nadia Null**: Missing data specialist
- **Otto Outlier**: Unusual observation expert
- **Val Validation**: Quality assurance
- **And others as the story requires...**

### Example Interaction

```
📖 Chapter 3: The Fermentation Files

You arrive at BioPharm Industries where Dr. Chen looks worried...

[Story narrative continues...]

What do you do?

A) Apply PCA to find patterns
B) Plot each variable individually
C) Run a random forest immediately
D) Ask for more data

Your choice (A/B/C/D):
```

### Session Management

- Save progress after each chapter
- Allow replaying chapters for better scores
- Show total adventure progress

Start or continue your adventure now!
