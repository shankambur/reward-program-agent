import streamlit as st
from dotenv import load_dotenv
import os

from agent import run_agent


st.title("Reward Program Agent")

print("==== Load Env ====")
load_dotenv()


print("get API key")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("OPENAI_API_KEY not found in .env file")
    st.stop

question = st.text_input(
    "Ask a reward program question"
)


if st.button("Submit"):

    if not question:
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Investigating reward data..."):
        answer = run_agent(question)

    st.markdown(answer)