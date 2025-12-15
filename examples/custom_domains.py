"""
Example: Custom domains and advanced routing
"""

from enum import Enum
from smart_router import SmartRouter, ToolRegistry, RouterConfig

# Define custom domains for your use case
class MyCustomDomains(str, Enum):
    """Custom domain taxonomy for e-commerce application"""
    INVENTORY = "inventory"
    ORDERS = "orders"
    CUSTOMERS = "customers"
    ANALYTICS = "analytics"
    SHIPPING = "shipping"
    PAYMENTS = "payments"

# Create registry with custom domains
registry = ToolRegistry()

# Inventory domain
registry.register_tool("check_stock", MyCustomDomains.INVENTORY, "Check product stock levels")
registry.register_tool("update_inventory", MyCustomDomains.INVENTORY, "Update inventory quantities")
registry.register_tool("get_low_stock_items", MyCustomDomains.INVENTORY, "Get items with low stock")

# Orders domain
registry.register_tool("create_order", MyCustomDomains.ORDERS, "Create a new order")
registry.register_tool("get_order_status", MyCustomDomains.ORDERS, "Get order status by ID")
registry.register_tool("cancel_order", MyCustomDomains.ORDERS, "Cancel an order")

# Customers domain
registry.register_tool("get_customer_info", MyCustomDomains.CUSTOMERS, "Get customer information")
registry.register_tool("update_customer", MyCustomDomains.CUSTOMERS, "Update customer details")
registry.register_tool("get_customer_orders", MyCustomDomains.CUSTOMERS, "Get all orders for a customer")

# Analytics domain
registry.register_tool("get_sales_report", MyCustomDomains.ANALYTICS, "Get sales analytics report")
registry.register_tool("get_top_products", MyCustomDomains.ANALYTICS, "Get top selling products")
registry.register_tool("get_revenue_metrics", MyCustomDomains.ANALYTICS, "Get revenue metrics")

# Shipping domain
registry.register_tool("track_shipment", MyCustomDomains.SHIPPING, "Track shipment status")
registry.register_tool("calculate_shipping", MyCustomDomains.SHIPPING, "Calculate shipping cost")

# Payments domain
registry.register_tool("process_payment", MyCustomDomains.PAYMENTS, "Process a payment")
registry.register_tool("refund_payment", MyCustomDomains.PAYMENTS, "Refund a payment")

print(f"✅ Registered {registry.total_tools} tools across {len(MyCustomDomains)} custom domains")

# Configure router with custom settings
config = RouterConfig(
    llm_provider="openai",
    model="gpt-4o-mini",
    temperature=0.05,  # Lower temperature for more consistent routing
    max_domains=3,
    confidence_threshold=0.75
)

router = SmartRouter(
    registry=registry,
    config=config,
    system_prompt_file="prompts/ecommerce_routing.md"  # Custom prompt
)

# Test with e-commerce queries
queries = [
    "Customer John Doe wants to track his order #12345",
    "Check if we have iPhone 15 in stock",
    "Process refund for order #67890",
    "Show me best selling products this month",
    "Customer email changed, need to update info",
]

print("\n" + "=" * 70)
print("E-COMMERCE ROUTING EXAMPLES")
print("=" * 70)

for query in queries:
    print(f"\n📝 Query: '{query}'")
    
    decision = router.route(query)
    
    print(f"   Domains: {[d.value for d in decision.domains]}")
    print(f"   Tools: {[t.name for t in decision.tools]}")
    print(f"   Confidence: {decision.confidence:.1%}")

    # Check if routing is uncertain
    if decision.confidence < 0.75:
        print(f"   ⚠️  Low confidence - consider asking for clarification")

print("\n" + "=" * 70)
print("✨ Custom domains allow domain-specific routing")
print("=" * 70)
