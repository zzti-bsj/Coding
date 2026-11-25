from mcp.server import MCPServer
import random

# create a mcp server
mcp = MCPServer("mysterious_numbers")

@mcp.tool()
async def get_mysterious_numbers():
    return round(random.random() * 100, 6)

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

