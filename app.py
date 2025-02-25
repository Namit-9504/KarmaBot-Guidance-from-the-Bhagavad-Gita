import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
from groq import Groq


# Groq API details
groq_api_key=os.getenv('GROQ_API_KEY')
GROQ_API_KEY = groq_api_key

st.set_page_config(page_title="KarmaBot: Guidance from the Bhagavad Gita", layout="wide")

st.title("🕉️ KarmaBot: Guidance from the Bhagavad Gita")
st.subheader("Seek wisdom from the Bhagavad Gita to overcome life's challenges.")

user_query = st.text_area("Enter your problem or question:", height=100)

client = Groq(
    api_key=GROQ_API_KEY,
)


st.sidebar.header("Select an AI Model",divider='rainbow')
models = [
    "qwen-2.5-32b", "qwen-2.5-coder-32b",
    "deepseek-r1-distill-qwen-32b", "deepseek-r1-distill-llama-70b",
    "gemma2-9b-it", "distil-whisper-large-v3-en",
    "llama-3.1-8b-instant", "llama-3.2-11b-vision-preview",
    "llama-3.2-1b-preview", "llama-3.2-3b-preview",
    "llama-3.2-90b-vision-preview", "llama-3.3-70b-specdec",
    "llama-3.3-70b-versatile", "llama-guard-3-8b",
    "llama3-70b-8192", "llama3-8b-8192",
    "mixtral-8x7b-32768",
    "whisper-large-v3", "whisper-large-v3-turbo"
]
selected_model = st.sidebar.selectbox("Choose a model:", models)
llm=selected_model
#llm="llama-3.3-70b-versatile"




def get_gita_guidance(input,llm):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": " You are KarmaBot, an AI assistant providing wisdom and guidance based on the Bhagavad Gita. \n    Your purpose is to help users overcome life challenges, mental distress, and confusion by offering relevant insights from the Gita.  \n    Provide answer for follwing situtation"
        },
        {
            "role": "user",
            "content":f"{input}"
        },
        
    ],
    stream=False,
    model=llm,)
    return chat_completion.choices[0].message.content

# Streamlit UI
if st.button("Get Guidance"):
    max_query_length = 1024
    if user_query.strip():
        with st.spinner("Fetching wisdom..."):
            response = get_gita_guidance(user_query,llm)
        st.success("Here's your guidance:")
        st.write(response)
    else:
        st.warning("Please enter a question or problem to get guidance.")

st.markdown("---")
st.caption("🤖 Powered by Groq API & Streamlit | Developed for Mental Well-being | Created By Namit Chaudhari ❤️")




