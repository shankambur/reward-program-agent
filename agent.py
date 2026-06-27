from langchain_openai import ChatOpenAI
from tools import (
    investigate_submission_tool,
    investigate_customer_tool,
    investigate_offer_tool
)
import json
from langchain_core.messages import SystemMessage, HumanMessage

TOOL_REGISTRY = {
    "investigate_submission": {
        "function": investigate_submission_tool,
        "args": []
    },
    "investigate_customer": {
        "function": investigate_customer_tool,
        "args": []
    },
    "investigate_offer": {
        "function": investigate_offer_tool,
        "args": []
    }
}

def run_agent(question, context=None):
    """
    Execute the complete agent workflow and return
    a natural language response.
    """
    if context is None:
       context = {}

    tool_calls = decide_tool(question)

    if not tool_calls:
       return "Sorry, I couldn't determine how to answer that question."

    tool_result = execute_tool(
        tool_calls[0],
        context
    )

    answer = generate_tool_response(
        question,
        tool_result
    )

    return answer
   

def decide_tool(question):
    try:

            llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0
            )
            
            tool_system_prompt = """
                You are a tool selection agent.

                Decide which tools are needed to answer the user's question.

                Available tools:

                    1. investigate_submission
                    Description: Investigates one transaction submission.
                    Args: submission_id: string
                    Example:
                    Question: Why did SUB0001 get credit?
                    Response:
                    [
                    {
                        "tool_name": "investigate_submission",
                        "args": {
                        "submission_id": "SUB0001"
                        }
                    }
                    ]

                    2. investigate_customer
                    Description:
                        Use when the user asks about a customer, customer details,
                        customer rewards, customer credits, customer activity,
                        or provides a customer identifier.

                    Args:
                        {
                        "customer_id": "<customer id>"
                        }
                    Example:
                    Question:
                        Show customer C1001 details
                            → investigate_customer

                        What rewards did customer C1002 receive?
                            → investigate_customer

                        Investigate customer C9999
                            → investigate_customer
                    Response:
                    [
                    {
                        "tool_name": "investigate_customer",
                        "args": {
                        "customer_id": "C1001"
                        }
                    }
                    ]

                    3. investigate_offer
                    Description: Investigates enrollments, eligibles, and credits for one offer.
                    Args: offer_id: string
                    Example:
                    Question: Show offer OFF600 details
                    Response:
                    [
                    {
                        "tool_name": "investigate_offer",
                        "args": {
                        "offer_id": "OFF600"
                        }
                    }
                    ]

                Return JSON only.

                Format:
                [
                {
                    "tool_name": "tool_name_here",
                    "args": {}
                }
                ]

                If no tool is needed, return:
                []
                """

            tool_user_prompt = f"""
                    User Question:
                    {question}
                    """
            
            print("****** calling API to decide tool")
            response = llm.invoke(
                    [
                        SystemMessage(content=tool_system_prompt),
                        HumanMessage(content=tool_user_prompt)
                    ]
                )
            print("response.content=",response.content)
            return json.loads(response.content)
    except Exception as e:
            print("Tool parser error:", e)
            return []


def execute_tool(tool_call, context):
    print("*** execute_tool based on tool_call and context **")
    
    print("context=",context)
    tool_name = tool_call["tool_name"]
    llm_args = tool_call.get("args", {})
    print("tool_name=",tool_name)
    print("llm_args=",llm_args)
    if tool_name not in TOOL_REGISTRY:
        return f"Tool '{tool_name}' is not available."

    tool_config = TOOL_REGISTRY[tool_name]
    tool_function = tool_config["function"]
    print("tool_config=",tool_config)
    print("tool_function=",tool_function)

    context_kwargs = {
        arg: context[arg]
        for arg in tool_config["args"]
    }
    print("context_kwargs=",context_kwargs)

    final_kwargs = {
        **context_kwargs,
        **llm_args
    }

    print("final_kwargs=", final_kwargs)

    return tool_function(**final_kwargs)

def validate_tool_result(tool_name, result):
    if not isinstance(result, dict):
        return {
            "found": False,
            "message": "Invalid tool result"
        }

    return result


def generate_tool_response(question,tool_result):

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    
    prompt = f"""
        You are a helpful rewards investigation assistant.

        User Question:
        {question}

        Tool Result:
        {tool_result}

        Generate a clear natural language response for the user.

        Rules:
        - Do not mention internal tool names.
        - Keep the answer concise.
        - Summarize first.
        - Only show detailed records if the user explicitly asks for full details.
        - Do not list every raw field unless needed.
        - Do not ask the user if they want more details.
        - Do not end with follow-up questions.
        - Do not add phrases like "let me know", "if you want", or "would you like".
        - If the user asks "why", explain the business reason using the tool result.
        """
    print("****** calling API to generate human response")
    response = llm.invoke(prompt)

    return response.content
