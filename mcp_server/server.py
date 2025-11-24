"""MCP server entry point for Claude Desktop."""

import sys
from mcp.server.fastmcp import FastMCP
from .tools.property_info_tool import get_property_info

# Initialize MCP server
mcp = FastMCP(name="property-mcp-server")

# Register single tool
mcp.tool(
    name="get_property_info",
    description="Fetch property details from ATTOM given a full address.",
)(get_property_info)

# Run in stdio mode for Claude Desktop
if __name__ == "__main__":
    try:
        mcp.run()
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        sys.exit(1)
