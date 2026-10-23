import streamlit as st
from groq import Groq
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import re

# 1. Pull the hidden secure key from Streamlit Cloud Secrets
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("🔒 Secret API Key missing. Please set up GROQ_API_KEY in your Streamlit dashboard.")
    st.stop()

# 2. Establish Connections (Groq AI Engine & Google Sheets Pipeline)
client = Groq(api_key=GROQ_API_KEY)
conn = st.connection("gsheets", type=GSheetsConnection)

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
                # --- GOOGLE SHEETS PIPELINE DATA LOGGER ---
                # Fetch existing rows from the Google Sheet
                try:
                    existing_data = conn.read(worksheet="Sheet1", ttl="0d")
                    df = pd.DataFrame(existing_data)
                except Exception:
                    df = pd.DataFrame(columns=["Email", "Niche"])
                
                # Format the new captured user lead
                new_lead = pd.DataFrame([{"Email": user_email, "Niche": niche}])
                
                # Combine the data tables and write it back to your sheet cloud rows
                updated_df = pd.concat([df, new_lead], ignore_index=True)
                conn.update(worksheet="Sheet1", data=updated_df)
                
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
                st.success("🔥 Unique AI Script Generated Successfully! (Lead Logged)")
                
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
