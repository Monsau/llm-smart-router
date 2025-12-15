# Architecture

## Overview

LLM Smart Router uses a two-phase approach to reduce tool count:

```
Phase 1: Domain Classification
User Query → LLM → Domain(s) + Reasoning

Phase 2: Tool Selection
Filtered Domains → Relevant Tools
```

## Components

### 1. Tool Registry

**Purpose**: Central catalog of all available tools

```python
class ToolRegistry:
    def register_tool(name, domain, description, tags)
    def get_tools_by_domain(domain) → List[ToolMetadata]
    def get_tools_by_domains(domains) → List[ToolMetadata]
```

**Storage**: In-memory dictionary
```
{
    AGDomain.MAAG: [tool1, tool2, ...],
    AGDomain.LAAG: [tool3, tool4, ...],
    ...
}
```

### 2. Smart Router

**Purpose**: Route queries to relevant tools

```python
class SmartRouter:
    def route(query: str) → RoutingDecision
```

**Process**:
1. Build domain taxonomy description
2. Send query + taxonomy to LLM
3. Parse structured response (JSON)
4. Fetch tools from registry
5. Return RoutingDecision

### 3. Data Models

#### AGDomain (Enum)
```python
class AGDomain(str, Enum):
    MAAG = "metrics_and_analytics"      # Monitoring
    LAAG = "logs_and_application"       # Logging
    CAAG = "code_and_architecture"      # Source code
    SAAG = "search_and_api"             # External APIs
    # ... 21 total domains
```

#### ToolMetadata
```python
class ToolMetadata:
    name: str
    domain: AGDomain
    description: str
    tags: List[str]
```

#### RoutingDecision
```python
class RoutingDecision:
    domains: List[AGDomain]       # Selected domains
    tools: List[ToolMetadata]     # Filtered tools
    confidence: float             # 0.0-1.0
    reasoning: str                # LLM explanation
```

## Routing Algorithm

### Input
- User query: `"API response time increased since deployment"`
- Registered tools: 93 across 12 domains

### Step 1: Build Context
```python
context = """
MAAG (Metrics & Analytics):
  - get_cpu_usage: Get CPU metrics
  - get_memory_usage: Get memory stats
  - get_api_latency: Get API response times

CAAG (Code & Architecture):
  - get_recent_commits: Get git history
  - get_changed_files: Files modified in commit
  
LAAG (Logs & Application):
  - search_logs: Search application logs
  - get_error_logs: Get error traces
...
"""
```

### Step 2: LLM Call
```python
prompt = f"""
Query: {query}

Available domains: {context}

Which domains are relevant? Return JSON:
{{
    "domains": ["MAAG", "CAAG"],
    "confidence": 0.95,
    "reasoning": "Query mentions API performance and deployment..."
}}
"""
```

### Step 3: Parse Response
```json
{
    "domains": ["MAAG", "CAAG", "LAAG"],
    "confidence": 0.92,
    "reasoning": "Need metrics, code changes, and logs"
}
```

### Step 4: Filter Tools
```python
relevant_tools = []
for domain in ["MAAG", "CAAG", "LAAG"]:
    relevant_tools += registry.get_tools_by_domain(domain)

# Result: 5 tools instead of 93
```

### Output
```python
RoutingDecision(
    domains=[MAAG, CAAG, LAAG],
    tools=[get_cpu_usage, get_api_latency, get_recent_commits, 
           get_changed_files, search_logs],
    confidence=0.92,
    reasoning="..."
)
```

## Performance Optimization

### 1. Caching (Future)
```python
# Cache routing decisions
cache_key = hash(query + str(registered_tools))
if cache_key in cache:
    return cache[cache_key]
```

### 2. Parallel Domain Analysis
```python
# Analyze multiple potential domains in parallel
async def analyze_domains(query, domains):
    tasks = [analyze_domain(query, d) for d in domains]
    results = await asyncio.gather(*tasks)
```

### 3. Early Stopping
```python
# Stop if confidence is very high
if decision.confidence > 0.95:
    return decision  # No need for refinement
```

## LLM Provider Integration

### OpenAI
```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.1
)
```

### Groq
```python
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
response = client.chat.completions.create(...)
```

### Anthropic
```python
from anthropic import Anthropic
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
response = client.messages.create(...)
```

### Local (Ollama)
```python
response = requests.post(
    "http://localhost:11434/api/chat",
    json={"model": "llama3:70b", "messages": [...]}
)
```

## Error Handling

### Low Confidence
```python
if decision.confidence < threshold:
    # Option 1: Use all tools (safe fallback)
    return RoutingDecision(tools=all_tools, confidence=0.0)
    
    # Option 2: Ask user for clarification
    return {"error": "Query ambiguous, please clarify"}
```

### LLM Failure
```python
try:
    decision = router.route(query)
except LLMError:
    # Fallback: Use heuristics
    domains = keyword_matching(query, domain_keywords)
    tools = registry.get_tools_by_domains(domains)
```

## Metrics

Track routing performance:
- **Latency**: Time to route query
- **Reduction**: % of tools filtered
- **Confidence**: Average confidence score
- **Cache Hit Rate**: % of cached responses

```python
metrics = {
    "avg_latency": 187,  # ms
    "avg_reduction": 95.8,  # %
    "avg_confidence": 0.89,
    "cache_hit_rate": 0.42
}
```
