"""Mood2Emoji — kid-safe app mapping sentences to emojis with sentiment analysis."""
import re
from textblob import TextBlob
import streamlit as st

BAD_WORDS = {"hate", "stupid", "idiot", "dumb", "kill", "damn", "crap", "sucks"}
POS_WORDS = {"happy", "good", "great", "love", "awesome", "nice", "fun", "yay"}
NEG_WORDS = {"sad", "bad", "sorry", "hate", "angry", "upset", "terrible"}

def contains_bad_words(text):
    """Check for inappropriate words."""
    words = re.findall(r"\b\w+\b", text.lower())
    matches = sorted(set(w for w in words if w in BAD_WORDS))
    return (len(matches) > 0, matches)

def analyze_sentiment(text):
    """Analyze sentiment using TextBlob with rule-based fallback."""
    try:
        return TextBlob(text).sentiment.polarity
    except:
        words = re.findall(r"\b\w+\b", text.lower())
        score = sum(1 for w in words if w in POS_WORDS) - sum(1 for w in words if w in NEG_WORDS)
        return max(-1.0, min(1.0, score / max(1, abs(score)))) if score else 0.0

def mood_from_polarity(p):
    """Map polarity to emoji and explanation."""
    return ("😀", "Sounds happy!") if p >= 0.2 else ("😞", "Sounds sad.") if p <= -0.2 else ("😐", "Seems neutral.")

def main():
    st.set_page_config(page_title="Mood2Emoji", page_icon="🙂", layout="centered")
    st.markdown("""<style>
        .stApp { background-color: #000000; color: #ffffff; }
        .big-emoji { font-size: 100px; text-align: center; margin: 30px 0; animation: bounce 0.5s; }
        @keyframes bounce { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.15); } }
        .result-text { font-size: 32px; text-align: center; font-weight: 700; color: #ff4444; 
                       margin: 15px 0; text-shadow: 0 0 10px rgba(255,68,68,0.3); }
        h1 { color: #ff4444 !important; text-align: center; font-size: 52px !important; 
             text-shadow: 0 0 20px rgba(255,68,68,0.4); margin-bottom: 5px !important; }
        .subtitle { color: #ffffff; text-align: center; font-size: 18px; margin-bottom: 30px; opacity: 0.9; }
        div[data-testid="stExpander"] { background-color: #1a1a1a; border-radius: 12px; 
                                        border: 2px solid #ff4444; color: #ffffff; }
        .stButton>button { background-color: #ff4444; color: #ffffff; border: none; 
                          padding: 14px 45px; font-size: 18px; border-radius: 30px; font-weight: 700; 
                          box-shadow: 0 4px 20px rgba(255,68,68,0.4); transition: all 0.3s; }
        .stButton>button:hover { background-color: #ff6666; transform: translateY(-3px); 
                                box-shadow: 0 6px 25px rgba(255,68,68,0.6); }
        .stTextInput>div>div>input { background-color: #1a1a1a; color: #ffffff; border: 2px solid #ff4444; 
                                     border-radius: 15px; font-size: 18px; padding: 12px; }
        .stTextInput>div>div>input:focus { border-color: #ff6666; box-shadow: 0 0 15px rgba(255,68,68,0.3); }
        .stTextInput label, .stCheckbox label { color: #ffffff !important; font-size: 16px; font-weight: 500; }
        p, li, div { color: #ffffff; }
        .stAlert { background-color: #1a1a1a; border-left: 4px solid #ff4444; color: #ffffff; }
    </style>""", unsafe_allow_html=True)
    
    st.title("🎭 Mood2Emoji")
    st.markdown('<p class="subtitle">Discover the emotion behind your words</p>', unsafe_allow_html=True)
    
    with st.expander("💡 Example Sentences"):
        st.markdown("😀 **Happy:** I love playing basketball!  \n😐 **Neutral:** Today was okay.  \n😞 **Sad:** I feel sad and lonely.")
    
    teacher_mode = st.checkbox("👨‍🏫 Teacher Mode")
    sentence = st.text_input("Enter a short sentence:", max_chars=200)
    analyzed = bad = False

    if st.button("Analyze") and sentence.strip():
        analyzed, (bad, matches) = True, contains_bad_words(sentence)
        if bad:
            st.warning("⚠️ Inappropriate word detected. Please try a different sentence.")
            st.write("Detected:", ", ".join(matches))
        else:
            polarity = analyze_sentiment(sentence)
            emoji, explanation = mood_from_polarity(polarity)
            st.markdown(f'<div class="big-emoji">{emoji}</div>', unsafe_allow_html=True)
            st.markdown(f'<p class="result-text">{explanation}</p>', unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; font-size: 18px; color: #cccccc;'>Score: <strong style='color: #ff4444;'>{polarity:.2f}</strong></p>", unsafe_allow_html=True)
            confidence = abs(polarity)
            if confidence > 0.5: st.success("🎯 High confidence")
            elif confidence > 0.2: st.info("📊 Moderate confidence")
            else: st.warning("🤔 Low confidence")

    if teacher_mode:
        st.markdown("---")
        st.markdown("### 🔍 How Mood2Emoji Works")
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown("**1️⃣ Input**  \n📝 Student types")
        col2.markdown("**2️⃣ Clean**  \n🛡️ Safety check")
        col3.markdown("**3️⃣ Analyze**  \n🧮 Sentiment score")
        col4.markdown("**4️⃣ Output**  \n😊 Emoji result")
        st.info("💡 **Teacher tip:** Discuss AI safety, bias, and limitations with students")
        
        if analyzed and sentence and not bad:
            words = re.findall(r"\b\w+\b", sentence.lower())
            pos = [w for w in words if w in POS_WORDS]
            neg = [w for w in words if w in NEG_WORDS]
            col_a, col_b = st.columns(2)
            col_a.write(f"✅ Positive: {', '.join(pos) if pos else 'None'}")
            col_b.write(f"❌ Negative: {', '.join(neg) if neg else 'None'}")
    
    st.markdown("---")
    st.caption("Classroom-safe demo for ages 12–16")

if __name__ == "__main__":
    main()
