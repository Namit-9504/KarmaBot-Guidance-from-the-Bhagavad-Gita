import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
from groq import Groq


# Groq API details
groq_api_key=os.getenv('GROQ_API_KEY')
GROQ_API_KEY = groq_api_key

st.set_page_config(page_title="KarmaBot: Guidance from the Bhagavad Gita", layout="centered")

st.title("🕉️ KarmaBot: Guidance from the Bhagavad Gita")
st.subheader("Seek wisdom from the Bhagavad Gita to overcome life's challenges.")

user_query = st.text_area("Enter your problem or question:", height=100)

client = Groq(
    api_key=GROQ_API_KEY,
)

llm="llama-3.3-70b-versatile"




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
st.caption("🤖 Powered by Groq API & Streamlit | Developed for Mental Well-being")




