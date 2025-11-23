"""FastAPI server with MCP integration."""

import uvicorn
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

from .tools import register_tools

# Initialize MCP server
mcp = FastMCP(
    name="property-mcp-server",
)

# Register tools
register_tools(mcp)

# Create FastAPI app and mount MCP
app = FastAPI(title="Property MCP Server", version="0.1.0")
app.mount("/mcp", mcp.streamable_http_app)


@app.get("/")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "service": "property-mcp-server"}


def main() -> None:
    """Run the server."""
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

