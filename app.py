import streamlit as st
from groq import Groq
import re

# Pull the hidden secure key from Streamlit Cloud Secrets
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("🔒 Secret API Key missing. Please set up GROQ_API_KEY in your Streamlit dashboard.")
    st.stop()

# Initialize the Groq AI Engine
client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="ViralCraft AI", page_icon="🚀", layout="centered")

st.title("🚀 ViralCraft AI")
st.subheader("Generate Custom Short-Form Scripts with Live AI")
st.write("The ultimate tool for TikTok, Reels, and YouTube Shorts creators.")

# Sidebar Configuration
st.sidebar.header("🎯 Target Audience & Niche")
niche = st.sidebar.selectbox(
    "Select your niche:",
    ["Personal Finance", "Fitness & Health", "Tech & AI", "Business & Startups", "Lifestyle & Travel"]
)

intensity = st.sidebar.slider("Hook Aggression/Curiosity Level (1-5)", 1, 5, 3)

st.write("---")

# Lead Capture Visual Interface
st.markdown("### 🔑 Unlock Your AI Script Generator")
st.write("Enter your business email below to connect to the elite AI trend-matching engine.")

user_email = st.text_input("📧 Your Email Address", placeholder="name@company.com")

# Helper function to check if the email format is correct
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

st.write("---")

# Main Action Trigger
if st.button("✨ Generate Custom AI Script", type="primary"):
    if not user_email:
        st.warning("⚠️ Please enter your email address to unlock the generator.")
    elif not is_valid_email(user_email):
        st.error("❌ The email address format looks invalid. Please enter a real email.")
    else:
        with st.spinner("AI is brainstorming your viral script..."):
            try:
                # --- SECURE SERVER LOG DATA PIPELINE ---
                # This safely logs your customer email lead straight into your private Streamlit Cloud console
                st.info(f"📥 Lead captured securely. Processing your request...")
                print(f"[DATA_LEAD_CAPTURED]: {user_email} | Niche: {niche}")
                
                # --- AI GENERATION BLOCK ---
                prompt = f"""
                Write a complete, highly engaging short-form video script for social media.
                Niche target: {niche}
                Hook Aggression/Curiosity Level: {intensity}/5 (Make it a strong pattern interrupter).
                
                Format your response explicitly like this:
                ### 🪝 Viral Hook
                (Write a single viral sentence that hooks the user immediately here)
                
                ### 📝 Video Script Body
                (Write the complete word-for-word narrative spoken text split into clear timing markers like [0:00-0:05]. Do not give general advice; write the exact script lines)
                
                ### 🚨 Strong Call to Action (CTA)
                (Write a highly converting action line driving comments or follows here)
                """
                
                completion = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": "You are an elite short-form content producer making million-view scripts for TikTok and Reels. Write the actual spoken words directly."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=600
                )
                
                ai_script = completion.choices.message.content
                st.success("🔥 Unique AI Script Generated Successfully!")
                
                st.markdown(ai_script)
                
                st.download_button(
                    label="💾 Download AI Script (.txt)",
                    data=ai_script,
                    file_name="viral_ai_script.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An unexpected server error occurred: {e}")
else:
    st.info("💡 Pick your configurations, type your email, and click 'Generate'.")
