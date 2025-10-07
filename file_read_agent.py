
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled, AsyncOpenAI, function_tool
from dotenv import load_dotenv
import asyncio
# Load environment
load_dotenv()
set_tracing_disabled(True)
# OpenAI / Gemini client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)
# Model setup
my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=my_model,
    model_provider=client,
    tracing_disabled=True
)
# Tool to read TXT file
@function_tool
def file_search_tool(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found!"
    except Exception as e:
        return f"Error reading file: {str(e)}"

# Agent setup with instructions
agent = Agent(
    name="shop_file_agent",
    tools=[file_search_tool],
    instructions="You are a shop assistant agent. Read the shop_data.txt file and answer any questions about item prices and availability."
)

# Run the agent
result = Runner.run_sync(agent, input="what is the price of Glue and pen(blue)?", run_config=config)
print(result.final_output)




 # yai nechay is agent ka urdu mai explaination hai
 

# 1. import os

# os: Python ka built-in module hai.

# Kaam: Operating system se related functions ke liye, jaise environment variables, file paths, etc.

# 2. from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled, AsyncOpenAI, function_tool

# Ye line agents library se kuch classes aur functions import karti hai.

# Agent: Ye aap ka AI agent banta hai jo tasks perform karega.

# Runner: Agent ko run karne ke liye use hota hai.

# OpenAIChatCompletionsModel: Model define karta hai jo AI responses generate karega.

# RunConfig: Agent ko run karne ka configuration store karta hai (jaise tracing, model, client).

# set_tracing_disabled: Tracing on/off karne ke liye function hai (debugging info show hoti hai ya nahi).

# AsyncOpenAI: Async (asynchronous) client jo API ke saath communicate karta hai.

# function_tool: Python function ko agent tool banane ke liye decorator.

# 3. from dotenv import load_dotenv

# load_dotenv: .env file se environment variables load karta hai (jaise API keys).

# 4. import asyncio

# Python ka module jo asynchronous programming ke liye hai.

# Kaam: Agent async functions run kar sake efficiently.

# 5. load_dotenv()

# .env file load karta hai taake API keys aur secrets Python mai available ho jayein.

# 6. set_tracing_disabled(True)

# Tracing ko disable karta hai.

# Matlab: debugging info console mai show nahi hogi.

# 7. OpenAI / Gemini client setup
# client = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta"
# )


# AsyncOpenAI: API client banta hai jo Gemini AI se connect karega.

# api_key=os.getenv("GEMINI_API_KEY"): .env file se GEMINI API key le raha hai.

# base_url: Gemini API ka URL jahan requests jayengi.

# 8. Model setup
# my_model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=client
# )


# OpenAIChatCompletionsModel: AI model define karta hai.

# model="gemini-2.0-flash": Specific AI model ka name.

# openai_client=client: Ye model us client se connect hoga jo upar banaya tha.

# 9. Run configuration
# config = RunConfig(
#     model=my_model,
#     model_provider=client,
#     tracing_disabled=True
# )


# RunConfig: Agent ko run karne ke liye configuration.

# model=my_model: Konsa model use karna hai.

# model_provider=client: Konsa API client use karna hai.

# tracing_disabled=True: Debug info nahi chahiye.

# 10. File search tool
# @function_tool
# def file_search_tool(file_path: str) -> str:
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             return f.read()
#     except FileNotFoundError:
#         return "File not found!"
#     except Exception as e:
#         return f"Error reading file: {str(e)}"


# @function_tool: Python function ko agent tool banata hai.

# file_search_tool(file_path: str) -> str: Ye function ek file_path leta hai aur content return karta hai (string).

# with open(file_path, "r", encoding="utf-8") as f: File read kar raha hai UTF-8 encoding ke saath.

# return f.read(): File ka saara content return karta hai.

# except FileNotFoundError: Agar file na mile to error message return kare.

# except Exception as e: Agar koi aur error ho to bhi message return kare.

# 11. Agent setup
# agent = Agent(
#     name="shop_file_agent",
#     tools=[file_search_tool],
#     instructions="You are a shop assistant agent. Read the shop_data.txt file and answer any questions about item prices and availability."
# )


# Agent: AI agent banaya.

# name="shop_file_agent": Agent ka name.

# tools=[file_search_tool]: Agent ke paas tool hai jo file read kar sakta hai.

# instructions: Agent ko bataya ke wo shop assistant hai aur questions ke jawab file se de.

# 12. Run the agent
# result = Runner.run_sync(agent, input="what is the price of Glue and pen(blue)?", run_config=config)
# print(result.final_output)


# Runner.run_sync: Agent ko synchronous mode mai run karta hai.

# agent: Kaunsa agent run karna hai.

# input="...": User ka question input.

# run_config=config: Run configuration use ho rahi hai.

# print(result.final_output): Agent ka final answer console mai print hota hai.