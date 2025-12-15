"""
Test data fixtures for unit tests
"""

import pytest
from smart_router import ToolRegistry, AGDomain, ToolMetadata


@pytest.fixture
def empty_registry():
    """Empty tool registry"""
    return ToolRegistry()


@pytest.fixture
def sample_registry():
    """Registry with sample tools"""
    registry = ToolRegistry()
    
    # MAAG tools
    registry.register_tool(
        "get_cpu_usage",
        AGDomain.MAAG,
        "Get CPU usage metrics",
        ["monitoring", "system"]
    )
    registry.register_tool(
        "get_memory_usage",
        AGDomain.MAAG,
        "Get memory usage metrics",
        ["monitoring", "system"]
    )
    
    # LAAG tools
    registry.register_tool(
        "search_logs",
        AGDomain.LAAG,
        "Search application logs",
        ["logs", "debugging"]
    )
    
    # CAAG tools
    registry.register_tool(
        "get_commits",
        AGDomain.CAAG,
        "Get git commits",
        ["git", "code"]
    )
    
    return registry


@pytest.fixture
def sample_tools():
    """List of sample tool metadata"""
    return [
        ToolMetadata(
            name="tool1",
            domain=AGDomain.MAAG,
            description="First tool",
            tags=["tag1"]
        ),
        ToolMetadata(
            name="tool2",
            domain=AGDomain.LAAG,
            description="Second tool",
            tags=["tag2"]
        ),
    ]


@pytest.fixture
def mock_llm_response():
    """Mock LLM response for routing"""
    return {
        "domains": ["MAAG", "LAAG"],
        "confidence": 0.92,
        "reasoning": "Query requires monitoring and log analysis"
    }
