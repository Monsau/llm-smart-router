# Quick Start

## Installation

```bash
pip install llm-smart-router
```

## 5-Minute Tutorial

### 1. Import

```python
from smart_router import SmartRouter, ToolRegistry, AGDomain
```

### 2. Register Tools

```python
registry = ToolRegistry()

# Add tools to domains
registry.register_tool("get_cpu", AGDomain.MAAG, "Get CPU usage")
registry.register_tool("search_logs", AGDomain.LAAG, "Search logs")
registry.register_tool("get_commits", AGDomain.CAAG, "Get git commits")
# ... add 90 more tools
```

### 3. Initialize Router

```python
router = SmartRouter(
    registry=registry,
    llm_provider="openai",
    model="gpt-4o-mini"
)
```

### 4. Route Queries

```python
decision = router.route("API slow since last commit")

print(decision.domains)  # [MAAG, CAAG, LAAG]
print(len(decision.tools))  # 5 tools instead of 93
print(decision.confidence)  # 0.92
```

### 5. Use with LangChain

```python
from langchain.agents import AgentExecutor

agent = AgentExecutor(
    tools=decision.tools,  # Only relevant tools
    llm=llm
)
result = agent.invoke({"input": "API slow since last commit"})
```

## Configuration

### Custom LLM Provider

```python
# Groq (fast, free)
router = SmartRouter(registry, llm_provider="groq", model="llama-3.3-70b")

# Anthropic
router = SmartRouter(registry, llm_provider="anthropic", model="claude-3-5-sonnet")

# Local Ollama
router = SmartRouter(registry, llm_provider="ollama", model="llama3:70b")
```

### Custom Domains

```python
from enum import Enum

class MyDomains(str, Enum):
    SALES = "sales"
    SUPPORT = "support"
    ANALYTICS = "analytics"

registry = ToolRegistry()
registry.register_tool("get_revenue", MyDomains.SALES, "Get sales data")
```

### Confidence Threshold

```python
from smart_router import RouterConfig

config = RouterConfig(
    confidence_threshold=0.8,  # Higher = more selective
    max_domains=2  # Limit domains per query
)

router = SmartRouter(registry, config=config)
```

## Next Steps

- [Architecture](architecture.md) - How it works
- [API Reference](api.md) - Full API documentation
- [Examples](../examples/) - More code examples
