"""
Basic usage example of LLM Smart Router
"""

from smart_router import SmartRouter, ToolRegistry, AGDomain

# Step 1: Create tool registry
registry = ToolRegistry()

# Step 2: Register tools by domain
# MAAG - Metrics & Monitoring
registry.register_tool(
    name="get_cpu_usage",
    domain=AGDomain.MAAG,
    description="Get current CPU usage percentage"
)
registry.register_tool(
    name="get_memory_usage",
    domain=AGDomain.MAAG,
    description="Get current memory usage stats"
)
registry.register_tool(
    name="get_disk_io",
    domain=AGDomain.MAAG,
    description="Get disk I/O statistics"
)

# LAAG - Logs & Analysis
registry.register_tool(
    name="search_logs",
    domain=AGDomain.LAAG,
    description="Search application logs by query"
)
registry.register_tool(
    name="get_error_count",
    domain=AGDomain.LAAG,
    description="Get count of errors in logs"
)
registry.register_tool(
    name="analyze_log_patterns",
    domain=AGDomain.LAAG,
    description="Analyze patterns in log files"
)

# CAAG - Code & Changes
registry.register_tool(
    name="get_recent_commits",
    domain=AGDomain.CAAG,
    description="Get recent git commits"
)
registry.register_tool(
    name="get_code_changes",
    domain=AGDomain.CAAG,
    description="Get code changes between commits"
)

# SAAG - Security
registry.register_tool(
    name="scan_vulnerabilities",
    domain=AGDomain.SAAG,
    description="Scan for security vulnerabilities"
)
registry.register_tool(
    name="check_permissions",
    domain=AGDomain.SAAG,
    description="Check file and user permissions"
)

print(f"✅ Registered {registry.total_tools} tools across {len(AGDomain)} domains")

# Step 3: Initialize router
router = SmartRouter(
    registry=registry,
    llm_provider="openai",  # or "groq", "anthropic"
    model="gpt-4o-mini",
    temperature=0.1
)

# Step 4: Route queries
queries = [
    "What's the CPU usage?",
    "Check for errors in logs",
    "API slow since last commit",
    "Scan for security issues"
]

print("\n" + "=" * 60)
print("ROUTING EXAMPLES")
print("=" * 60)

for query in queries:
    print(f"\n📝 Query: '{query}'")
    
    # Route the query
    decision = router.route(query)
    
    print(f"   Domains: {[d.value for d in decision.domains]}")
    print(f"   Tools: {[t.name for t in decision.tools]} ({len(decision.tools)} selected)")
    print(f"   Confidence: {decision.confidence:.1%}")
    print(f"   Reasoning: {decision.reasoning}")

print("\n" + "=" * 60)
print(f"✨ Reduced from {registry.total_tools} tools to 3-8 relevant tools per query")
print("=" * 60)
