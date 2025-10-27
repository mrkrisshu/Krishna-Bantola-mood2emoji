# Mood2Emoji

A kid-safe, minimal web app that converts a short sentence into a friendly emoji (😀 😐 😞) and a one-line explanation. Built with Python and Streamlit for classroom use. Includes a Teacher Mode to explain the simple 4-step pipeline.

## Project overview and objectives
- **Objective**: Teach basic ideas of text classification and safety by mapping simple sentences to mood emojis.
- **Audience**: Students ages 12–16.
- **Key ideas covered**: input cleaning (safety), simple sentiment analysis, mapping outputs to human-friendly feedback, and AI ethics (content safety and limitations).

## What the app does
1. Checks the input for inappropriate/bad words. If found, it blocks the output and shows a gentle warning.
2. If clean, it analyzes the sentiment (TextBlob is used; a lightweight fallback is included).
3. Maps the sentiment polarity to an emoji and a short, kid-friendly explanation.

## Setup (local)
Requires Python 3.9+.

Open a terminal (PowerShell on Windows) and run:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

On first deploy you can test sentences such as:
- "I had a great day!" → 😀 Sounds happy!
- "It was okay." → 😐 Seems neutral.
- "I feel sad today." → 😞 Sounds sad.

## Run on Streamlit Cloud
1. Create a GitHub repo with these files (`app.py`, `requirements.txt`, `README.md`, `lesson_plan.pdf`).
2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud) and link the repo.
3. Set the main file to `app.py`. Streamlit Cloud will install dependencies from `requirements.txt` and run the app.

## How kids learn from this app
- **Immediate, visual feedback** links text to mood through emojis.
- **Teacher Mode** provides a simple pipeline to discuss each step.
- Encourages discussion about why some sentences are blocked and why sentiment analysis can be imperfect.
- **Builds computational thinking**: Students see input → process → output in action.
- **Introduces AI ethics**: Safety filters, bias, and limitations are discussed openly.

## Pedagogical Framework
This app follows a **constructivist learning approach**:
1. **Explore**: Students experiment with different sentences
2. **Explain**: Teacher Mode reveals the "how" behind the magic
3. **Elaborate**: Students discuss edge cases and limitations
4. **Evaluate**: Students assess when the app works well and when it doesn't

This aligns with Codingal's mission to make AI education accessible and engaging for young learners.

## Suggested classroom activities (brief)
- **Pair up**: students write friendly sentences and test the app.
- **Discuss mistakes**: show examples where the app misinterprets tone, and ask why.
- **Safety chat**: discuss why bad-word filtering matters and its limits.

## Lesson plan (60 minutes)
See `lesson_plan.md` for a full lesson you can turn into PDF (`lesson_plan.pdf`).

## Known limitations
- The bad-words list is small and not exhaustive — false negatives/positives are possible.
- Sentiment analysis is simple; sarcasm, context, and complex sentences may be misclassified.
- For production, expand safety lists, include human moderation, and consider privacy policies.

## Future Enhancements
- **Multilingual support** (Hindi, Spanish, etc.)
- **Customizable safety filters** for different schools
- **Teacher dashboard** to track common misclassifications
- **Student progress tracking** (with proper consent/privacy)
- **Integration with Codingal's LMS** for seamless classroom use

## Teaching notes & ethics
- Emphasize responsible AI use: safety, consent, and limitations.
- Remind students that tools can make mistakes and that human judgment matters.

## License & credit
This is a classroom demo created for a take-home assignment. Feel free to adapt for teaching.
