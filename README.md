# glee-mcp-agentic-ai

1. terminal> uv init
2. create virtual environment: terminal > uv venv
3. activate : Activate with: source .venv/bin/activate
4. add libraries : uv add "mcp[cli]" - we are going to use specific library called "FastApi"
5. refer this github for more mcp setup - https://github.com/modelcontextprotocol/python-sdk
6. doc string is more important becuase LLM will understand based on the doc string values
7. How to run MCP: 
8.      MCP Inspector
9.         uv run mcp dev server/weather.py
10.         ERROR    npx not found. Please ensure Node.js and npm are properly installed and added   cli.py:296
                to your system PATH. You may need to restart your terminal after installation.
11. Install Node.js and npm
        brew install node
12. Install Homebrew, If brew is not installed/ available in macbook: 
13.     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        Password : macbook password
14. Add Homebrew to your PATH (Critical for M1/M2/M3 Macs)
        (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/mahathi/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

15. Install Node.js and npm
        brew install node
16. Verify the installation
        node -v
        npm -v
        See: v25.2.1
13. Restart your tertminal
14. How to run MCP: 
        MCP Inspector
        uv run mcp dev server/weather.py
15. Need to install the following packages:
        @modelcontextprotocol/inspector@0.18.0
        Ok to proceed? (y) y
---------------------------------------------------
16. MCP Inspector: uv run mcp dev server/weather.py
17. Claude App : uv run mcp install server/weather.py
18. Can we directly integrated with command line
        for this approach we are using client
19. client.py is needed to integrated with mcp server and do LLM integration
20. We need one mere library: MCP-USE - https://github.com/mcp-use/mcp-use
        MCP USE: open source way to connect any LLM to any MCP server and build custom agent that have tool access without using closed source or application clients
21. terminal:> uv add mcp-use
22. terminal:> uv add lanchain_groq (since we're using GROQ LLM)
23. termanal:> uv add nest_asyncio