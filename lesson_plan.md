# Lesson Plan: Build a Mood2Emoji App — Intro to Text Classification

**Title**: Build a Mood2Emoji App — Intro to Text Classification  
**Audience**: Ages 12–16  
**Duration**: 60 minutes

## Objective
Students will understand a simple text-classification pipeline and try a kid-safe demo that maps sentences to emojis. They'll explore why content safety matters and see how algorithms can make mistakes.

## Concepts introduced
- **Input → Cleaning (safety) → Analysis (sentiment) → Output**
- Sentiment polarity (positive/neutral/negative)
- Why filters and human oversight are important (ethics & safety)
- Limitations of automated text understanding

## Materials
- A computer with Internet, Python 3.9+, or access to Streamlit Cloud
- Project URL or local copy of `app.py`

## Activity plan & timing

### 1. Warm-up (5 minutes)
- Quick brainstorm: "What makes a sentence sound happy or sad?"
- Write a few words on the board and ask students to vote on mood.

### 2. Demo (10 minutes)
- Show the app, type in 3–4 example sentences. Toggle Teacher Mode.
- Ask students to predict what emoji the app will return before clicking "Analyze."
- Example sentences:
  - "I love recess!" (expected: 😀)
  - "Today was boring." (expected: 😐)
  - "I feel sad and tired." (expected: 😞)

### 3. Hands-on pairs (15 minutes)
- Students work in pairs to try their own sentences.
- **Task**: Create 3 sentences the app classifies as happy, neutral, and sad.
- Encourage creativity and testing edge cases.

### 4. Discussion: Safety & ethics (10 minutes)
- Show an example with a "not-appropriate" word and how the app blocks it.
- Discuss:
  - Why do we need safety filters?
  - Can filters make mistakes? (False positives/negatives)
  - What role does human judgment play?

### 5. Reflection & extension (15 minutes)
- Have pairs pick **one misclassified sentence** and discuss why the app got it wrong.
- Optional challenge: Suggest improvements (bigger safety list, more context, teacher review).
- Share findings with the class.

### 6. Wrap-up (5 minutes)
- Key takeaways:
  - Models can help but must be used responsibly.
  - Human judgment matters.
  - AI systems have limitations and can make mistakes.

## Learning outcomes
By the end of this lesson, students will be able to:
- Recognize a simplified ML pipeline for text processing.
- Understand basic sentiment mapping to human-friendly outputs.
- Appreciate content safety and that models make mistakes.
- Practice clear explanations and critical thinking about algorithmic output.

## Assessment ideas
- **Short exit ticket**: Students write one sentence describing one strength and one limitation of the app.
- **Optional homework**: Improve the app's safety list and bring 5 test sentences to next class.

## Ethical emphasis
- Respect for students' words and privacy.
- Avoid using personal or sensitive content in examples.
- Understand that filters may wrongly block or allow content; always include human review.

## Notes for teachers
- Keep the activity light and safe — avoid asking students to type personal or traumatic experiences.
- Use Teacher Mode to lead a short explanation of each pipeline step.
- Encourage curiosity about how to make systems safer and fairer.
- Consider having students sign a brief "digital citizenship" agreement before using the app.

## Extensions (for advanced classes)
- **Code exploration**: Show students the `app.py` file and walk through key functions.
- **Data collection**: Have students label 20 sentences and calculate the app's accuracy.
- **Improvement project**: Students propose and implement one improvement (e.g., handling negation like "not happy").

## Differentiation Strategies

### For struggling learners:
- Provide sentence templates to fill in (e.g., "I feel ___ because ___")
- Focus on the emoji output rather than technical details
- Pair with a peer mentor

### For advanced learners:
- Challenge them to "break" the app with edge cases
- Have them design an improved bad-words detection system
- Ask them to research how production sentiment tools (like Google's Perspective API) work

## Assessment Rubric (for student activity)

| Criterion | Emerging (1) | Developing (2) | Proficient (3) | Advanced (4) |
|-----------|--------------|----------------|----------------|--------------|
| Understanding of pipeline | Can't explain steps | Names steps but unclear | Explains all 4 steps clearly | Explains steps + suggests improvements |
| Safety awareness | Doesn't recognize need | Knows filters exist | Explains why filters matter | Discusses trade-offs & limitations |
| Critical thinking | Accepts all outputs | Notices some errors | Documents multiple errors | Proposes systematic fixes |

---

**End of Lesson Plan**
