# file_reading_agent
an AI shop assistant agent that reads item data from a text file and answers questions about prices and availability. ✅  Simple AI agent that uses Gemini API to read shop data from a text file.  File-based AI assistant for querying shop inventory and prices using Gemini 2.0 model.  Shop assistant agent built with OpenAI Agents SDK 
📌 Overview

This project defines an AI Shop Assistant Agent that can read data from a text file (shop_data.txt) and answer user queries about item prices and availability.
It uses the OpenAI Agents SDK (or compatible library) and integrates a simple file-reading tool to fetch information dynamically.

⚙️ How It Works

The environment variables are loaded using dotenv (for API keys).

A Gemini model (gemini-2.0-flash) is configured through AsyncOpenAI.

A custom tool file_search_tool reads data from a .txt file.

The Agent uses this tool to respond to user questions related to the shop data.

The Runner executes the agent with a sample query.
