import streamlit as st
from groq import Groq
import re

# Safely extract the hidden token key from the Streamlit Cloud dashboard backend
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("🔒 Secret API Key missing. Please set up GROQ_API_KEY in your Streamlit dashboard settings.")
    st.stop()

# Initialize our high-speed Groq AI client engine
client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="BizViral AI", page_icon="🚀", layout="centered")

st.title("🚀 BizViral AI")
st.subheader("Generate High-Converting Local Business Scripts with Live AI")
st.write("Turn casual scrollers into paying customers for local businesses and agencies.")

# Sidebar Configuration panel layout - UPGRADED WITH SPECIFIC BUSINESS NICHES
st.sidebar.header("🎯 Target Industry & Business")
niche = st.sidebar.selectbox(
    "Select your business niche:",
    [
        "Real Estate (Agents & Brokers)", 
        "Gyms & Fitness Centers", 
        "Dental & Medical Clinics", 
        "Restaurants & Cafes",
        "Personal Finance & Coaching", 
        "Tech & AI Startups"
    ]
)

intensity = st.sidebar.slider("Hook Aggression/Curiosity Level (1-5)", 1, 5, 3)

st.write("---")

# Front-end user lead acquisition entry interface
st.markdown("### 🔑 Unlock Your Business AI Script Generator")
st.write("Enter your business email below to connect to our local-lead generation AI engine.")

user_email = st.text_input("📧 Your Email Address", placeholder="name@company.com")

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

st.write("---")

# Core operational trigger button logic
if st.button("✨ Generate Business‑Getting AI Script", type="primary"):
    if not user_email:
        st.warning("⚠️ Please enter your email address to unlock the generator.")
    elif not is_valid_email(user_email):
        st.error("❌ The email address format looks invalid. Please enter a real email.")
    else:
        with st.spinner("AI is crafting your industry-specific sales script..."):
            try:
                st.info(f"📥 Lead captured securely. Processing your request...")
                print(f"[DATA_LEAD_CAPTURED]: {user_email} | Niche: {niche}")
                
                # Custom industry-tailored prompt structure
                prompt = f"""
                Write a complete, highly engaging short-form video sales script (TikTok/Reels/Shorts) designed to get localized client leads.
                Business Industry/Niche: {niche}
                Hook Aggression Level: {intensity}/5 (Make it a powerful local pattern interrupter).
                
                Format your response explicitly using these markdown headers:
                ### 🪝 Local Business Hook  
                (Write 1 psychological sentence tailored to this industry that makes local viewers stop scrolling)
                
                ### 📝 Lead-Gen Video Script Body  
                (Write the complete word-for-word spoken narrative script text split into precise timing blocks like [0:00-0:05]. Make it sound natural, professional, and persuasive. Write the exact lines the business owner should say)
                
                ### 🚨 Conversion Call to Action (CTA)  
                (Write a highly specific, high-conversion action line forcing viewers to comment a keyword or click a link in bio for a free consult/voucher/guide)
                """
                
                completion = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": "You are a master local direct-response marketer and elite scriptwriter who specializes in generating localized customer leads for physical businesses via short-form video ads."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=600
                )
                
                ai_script = completion.choices.message.content
                st.success("🔥 Local Business Script Generated Successfully!")
                st.markdown(ai_script)
                
                st.download_button(
                    label="💾 Download Business Script (.txt)",
                    data=ai_script,
                    file_name="local_business_script.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An unexpected server error occurred: {e}")
else:
    st.info("💡 Pick your targeted configurations, type your email, and click 'Generate'.")
