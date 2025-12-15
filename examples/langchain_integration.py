"""
Example: Integration with LangChain Agent
"""

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool

from smart_router import SmartRouter, ToolRegistry, AGDomain

# Define actual tool functions
def get_cpu_usage() -> str:
    """Get CPU usage"""
    return "CPU Usage: 45%"

def search_logs(query: str) -> str:
    """Search logs"""
    return f"Found 3 log entries matching '{query}'"

def get_recent_commits() -> str:
    """Get recent commits"""
    return "Last commit: 'Fix API performance' by John Doe"

# Create LangChain tools
langchain_tools = [
    Tool(name="get_cpu_usage", func=get_cpu_usage, description="Get current CPU usage"),
    Tool(name="search_logs", func=search_logs, description="Search application logs"),
    Tool(name="get_recent_commits", func=get_recent_commits, description="Get recent git commits"),
    # ... 90 more tools
]

# Setup Smart Router
registry = ToolRegistry()
for tool in langchain_tools:
    # Map tools to domains (example: simple keyword matching)
    if "cpu" in tool.name or "memory" in tool.name:
        domain = AGDomain.MAAG
    elif "log" in tool.name:
        domain = AGDomain.LAAG
    elif "commit" in tool.name or "code" in tool.name:
        domain = AGDomain.CAAG
    else:
        domain = AGDomain.IAAG
    
    registry.register_tool_from_langchain(tool, domain)

router = SmartRouter(registry=registry)

# User query
user_query = "API performance degraded after last deployment"

# Step 1: Route to get relevant tools
print(f"Query: {user_query}")
print(f"Total tools available: {len(langchain_tools)}")

decision = router.route(user_query)
print(f"Selected domains: {[d.value for d in decision.domains]}")
print(f"Reduced to {len(decision.tools)} tools")

# Step 2: Create LangChain agent with only relevant tools
llm = ChatOpenAI(model="gpt-4o", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use the provided tools to answer questions."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_functions_agent(llm, decision.tools, prompt)
executor = AgentExecutor(agent=agent, tools=decision.tools, verbose=True)

# Step 3: Execute
print("\n" + "=" * 60)
print("AGENT EXECUTION")
print("=" * 60)

result = executor.invoke({"input": user_query})
print(f"\nResult: {result['output']}")

print("\n✨ Success! Agent used only relevant tools instead of all 93 tools")
