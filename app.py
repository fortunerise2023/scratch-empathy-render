
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Scratch Empathy Project", layout="wide")

# === Cover ===
st.image("https://raw.githubusercontent.com/fortunerise2023/scratch-empathy-render/main/assets/scratch-cat.jpg", width=100)
st.title("Scratch Empathy Project")
st.markdown("### Inclusive Coding Education for Neurodiverse Learners")

st.markdown("""
> *“Coding isn’t just for the cognitively typical. It’s a new language — and everyone deserves a voice.”*  
> — **Yixuan Li**, Founder and Instructor
""")

st.divider()

# === Project Summary ===
st.header("📘 Project Introduction")

st.markdown("""
The **Scratch Empathy Project** is a student-driven initiative developed by **Yixuan Li**, a high school student at *Beijing JunChen International Bilingual School*.  
It uses MIT Scratch to teach children on the autism spectrum logical reasoning, creativity, and digital self-expression through code.

Rooted in a family background of both computer science and developmental psychology, this project merges empathy with engineering. Over multiple months, Yixuan designed a five-module curriculum, taught sessions to neurodiverse learners, and measured engagement through structured data feedback.
""")

st.divider()

# === Curriculum Modules ===
st.header("📚 Curriculum Modules")
st.markdown("""
1. **Avatar Building & Character Logic** – personalization with events and triggers  
2. **Stage Animation** – visual storytelling using motion and control blocks  
3. **Sound Interaction** – audio response, reaction timing, and cognitive reward  
4. **Logic Puzzles** – hands-on problem solving with conditions and loops  
5. **Capstone Project** – each learner builds and demos their own Scratch game
""")

st.divider()

# === Data & Reflection ===
st.header("📊 Student Feedback & Focus Trends")

try:
    df = pd.read_csv("data/feedback.csv")
    st.markdown("**Average Attention Score per Module (scale 1–5):**")
    fig, ax = plt.subplots()
    df.groupby("Lesson")["AttentionScore"].mean().plot(kind="bar", color="#4c72b0", ax=ax)
    ax.set_ylabel("Avg. Score")
    ax.set_xlabel("Lesson #")
    ax.set_title("Focus Trend Across Lessons")
    st.pyplot(fig)

    with st.expander("📄 View Full Feedback Table"):
        st.dataframe(df)
except Exception as e:
    st.warning(f"Could not load feedback data: {e}")

st.divider()

# === Video Showcase ===
st.header("🎬 In-Class Demonstration Video")
st.video("https://www.youtube.com/watch?v=1rD2xf5qGC4")

st.divider()

# === Author Bio ===
st.header("👨‍💻 About the Creator")
st.markdown("""
**Yixuan Li** is a 15-year-old student currently studying at *Beijing JunChen International Bilingual School* (Class of 2026).  
With early exposure to programming and a home environment rich in cognitive science, he seeks to bridge technology and inclusion through education.

> “This project is my way of using code to build empathy — and giving kids who think differently a space to shine.”
""")

st.markdown("🔗 **Demo Website by Render** — Powered by Python + Streamlit")

st.caption("Made with ❤️ by Yixuan Li — All rights reserved.")
