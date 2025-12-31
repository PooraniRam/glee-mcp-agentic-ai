import asyncio

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from mcp_use import MCPAgent, MCPClient

import os

async def glee_chat():
    """Run the chat using MCPAgent's built-in conversation memory"""

    #Load environment variables for API Keys
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    #Config file
    config_file="server/weather.json"

    print("Initializing the chat ...")

    # Create MCP client and agent with memory enables
    client = MCPClient.from_config_file(config_file)

    llm = ChatGroq(model="llama-3.1-8b-instant")

    # Create Agent with memory_enables=true
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True # Enable built-in conversation memory
    )

    print("\n===Interactive Glee MCP Chat===")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear the conversation history")

    try:
        # Main chat loop
        while True:
            #Get user input
            user_input = input("\n You::: ")

            if user_input.lower() in ['exit', 'clear']:
                print("Ending Conversation ...")
                break

            if user_input.lower()=='clear':
                agent.clear_conversation_history()
                print("Conversation history cleared")
                continue
            
            #Get response from Agent
            print("\n Assistant: ", end="", flush=True)

            try:
                # Run the agent with user input (memory handling is automatic)
                response =  await agent.run(user_input) 
                print (response)

            except Exception as e:
                print("\n Error : {e}")
    finally:
        # Clean up
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(glee_chat())
