import streamlit as st
import google.generativeai as genai

# Set up page config
st.set_page_config(page_title="AI Code Reviewer", page_icon="🧑‍💻", layout="wide")

# Load API Key from Streamlit Secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

if not GOOGLE_API_KEY:
    st.error("⚠️ Google API Key not found! Add it in Streamlit secrets.")
    st.stop()

# Configure Google Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# AI System Prompt
sys_prompt = """
You are an AI Code Reviewer—sharp on bugs, obsessed with optimization, and dedicated to writing clean, efficient code. 🧑‍💻💡  
Your job is to **analyze, debug, and improve** code while providing clear, engaging explanations.  

✅ **Key Responsibilities:**  
- **Identify & fix errors** with explanations.  
- **Optimize performance** while following best practices.  
- **Suggest improvements** for readability and efficiency.  
- **If the code is perfect, respond with:** '✅ Code looks great! No issues found.'  
- **Use humor, analogies, and memes** to make reviews fun & engaging.  

🔥 **Personality:**  
- Be witty, friendly, and constructive.  
- If the code is bad, **roast it like a best friend**—but always provide solutions.  
- If the code is great, **hype up the user like they're the next tech legend.**  

🚀 **Response Format:**  
- Use **bold** and *italic* for emphasis.  
- Provide **examples & structured feedback** (e.g., ✅ Pros, ❌ Issues, 🔄 Fixes).  
"""

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #E0E0E0;
        font-family: 'Arial', sans-serif;
    }
    .stTextArea textarea {
        background-color: #1E1E1E;
        color: #E0E0E0;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #64FFDA;
        color: #121212;
        border-radius: 8px;
        font-size: 16px;
    }
    .stMarkdown {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("🔍 AI Code Reviewer")
st.write("🚀 Get AI-powered review on your code now")

# Code Input
code_input = st.text_area("CODE PLEASE:", height=200, placeholder="I won't judge if you paste your code here!...")

# Review Button
if st.button("Review Code 🚀"):
    if code_input.strip():
        st.info("Take a Deep Breath, your code is being reviewed.... ⏳")
        
        # AI Prompt with System Instructions
        prompt = sys_prompt + f"\n\nHere is your code for review Darling\n```python\n{code_input}\n```"

        try:
            # Get AI Response
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            feedback = response.text

            # Display AI Response
            st.subheader("🔍 AI Feedback")
            st.markdown(f'<div class="stMarkdown">{feedback}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

    else:
        st.warning("⚠️ Are you kidding, I'm missing the code here..")

# Footer
st.markdown("---")
st.write("📌 Developed by **Rutu** ❤️ using Google Gemini & Streamlit")
