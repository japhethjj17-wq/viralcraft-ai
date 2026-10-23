import streamlit as st
import random

st.set_page_config(page_title="ViralCraft AI", page_icon="🚀", layout="centered")

st.title("🚀 ViralCraft AI")
st.subheader("Generate High-Converting Short-Form Scripts in Seconds")
st.write("The ultimate tool for TikTok, Reels, and YouTube Shorts creators.")

st.sidebar.header("🎯 Target Audience & Niche")
niche = st.sidebar.selectbox(
    "Select your niche:",
    ["Personal Finance", "Fitness & Health", "Tech & AI", "Business & Startups", "Lifestyle & Travel"]
)

intensity = st.sidebar.slider("Hook Aggression/Curiosity Level", 1, 5, 3)

hooks_database = {
    "Personal Finance": [
        "The lazy way to make $100 a day without leaving your bed...",
        "Stop saving your money in a bank account. Do this instead.",
        "3 financial lies you were told by adults that are keeping you broke."
    ],
    "Fitness & Health": [
        "If you are still doing cardio to lose weight, please stop.",
        "Eat this one food before bed to burn fat while you sleep.",
        "The 4-minute morning routine that replaces an hour at the gym."
    ],
    "Tech & AI": [
        "This terrifying new AI tool is about to put millions out of a job.",
        "How I force ChatGPT to write all my emails perfectly.",
        "3 secret websites that feel illegal to know."
    ],
    "Business & Startups": [
        "How a 19-year-old built a $50k/month business in 2 weeks.",
        "The biggest marketing trap that kills 99% of new businesses.",
        "Steal this 3-step psychological trick to sell anything to anyone."
    ],
    "Lifestyle & Travel": [
        "Stop visiting Paris. Go to this secret European town instead.",
        "How to travel the world full-time for less than $800 a month.",
        "The airline hack they don't want you to find out about."
    ]
}

st.write("---")

if st.button("✨ Generate Viral Script Package", type="primary"):
    with st.spinner("Analyzing viral trends..."):
        selected_hook = random.choice(hooks_database[niche])
        st.success("🔥 Script Package Generated Successfully!")
        st.markdown(f"### 🪝 Viral Hook\n**\"{selected_hook}\"**")
        st.markdown("### 📝 Video Script Body")
        st.write("**[0:03 - Body Paragraph 1]:** Deliver on the promise of the hook immediately. Don't waste time introducing yourself. Give them the absolute best tip or shocking fact right away.")
        st.write("**[0:15 - Body Paragraph 2]:** Explain *how* to apply it. Use high-energy, simple words. Keep visual pacing fast.")
        st.markdown("### 🚨 Strong Call to Action (CTA)")
        st.write("**[0:25 - Outro]:** 'If you want the step-by-step guide for free, drop a comment below and follow for more daily blueprints.'")
        
        full_script = f"Niche: {niche}\n\nHook: {selected_hook}\n\nBody:\nDelivering the core value immediately...\nHow to apply it easily...\n\nCTA: Comment below and follow for more."
        st.download_button(
            label="💾 Download Script (.txt)",
            data=full_script,
            file_name="viral_script.txt",
            mime="text/plain"
        )
else:
    st.info("💡 Choose your niche on the left and click 'Generate' to create a high-retention video blueprint.")
