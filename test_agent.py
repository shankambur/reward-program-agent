from dotenv import load_dotenv
import os
from agent import (
    decide_tool,
    generate_tool_response,
    execute_tool
)

def callAgent(question):
    print("Start******* test full agent flow for the question=",question)
    tool_calls = decide_tool(question)
    tool_result = execute_tool(
        tool_calls[0],
        {}
    )
    response = generate_tool_response(
        question,
        tool_result
    )
    print(response)
    print("End****************End\n")


print("==== Load Env ====")
load_dotenv()


print("get API key")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("OPENAI_API_KEY not found in .env file")
    
    exit()
else:

    
    print("******* test decide tool for 'Show customer C1001 details' Start")
    print(decide_tool("Show customer C1001 details"))
    print("**************** End\n")

    print("******* test decide tool for 'Investigate offer OFF600' Start")
    print(decide_tool("Investigate offer OFF600"))
    print("**************** End\n")

    print("******* test decide tool for 'Why did SUB0001 get credit?' Start")
    print(decide_tool("Why did SUB0001 get credit?"))
    print("****************End\n")

    print("******* test execute_tool for 'investigate_customer' Start")
    tool_call = {
            "tool_name": "investigate_customer",
            "args": {
                "customer_id": "C1002"
            }
    }
    context = {}
    result = execute_tool(tool_call, context)
    print(result)
    print("****************End\n")

    print("******* test execute_tool for 'investigate_offer' Start")
    tool_call = {
            "tool_name": "investigate_offer",
            "args": {
                "offer_id": "OFF600"
            }
    }
    context = {}
    result = execute_tool(tool_call, context)
    print(result)
    print("****************End\n")



    print("******* test execute_tool for 'investigate_submission' Start")
    tool_call = {
            "tool_name": "investigate_submission",
            "args": {
                "submission_id": "SUB0001"
            }
    }
    context = {}
    result = execute_tool(tool_call, context)
    print(result)
    print("****************End\n")


    # test agent flow
    callAgent("Why did SUB0001 get credit?")
    callAgent("Show customer C1001 details")
    