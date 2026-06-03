import streamlit as st
from dotenv import load_dotenv
import os

from agent import (
    decide_tool,
    execute_tool,
    generate_tool_response
)

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

    tool_calls = decide_tool(question)

    if not tool_calls:
        st.error("No suitable tool found")
        st.stop()

    tool_result = execute_tool(
        tool_calls[0],
        {}
    )

    answer = generate_tool_response(
        question,
        tool_result
    )
    st.text(answer)