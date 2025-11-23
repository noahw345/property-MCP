"""FastAPI server with MCP integration."""

import json
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mcp import MCPServer

from .tools import get_comparables, get_property_info

# Initialize FastAPI app
app = FastAPI(title="Property MCP Server", version="0.1.0")

# Initialize MCP server
mcp_server = MCPServer("property-mcp-server")

# Register tools
mcp_server.add_tool(get_property_info)
mcp_server.add_tool(get_comparables)


@app.get("/")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "service": "property-mcp-server"}


@app.post("/mcp")
async def mcp_endpoint(request: Request) -> JSONResponse:
    """MCP endpoint for tool execution."""
    try:
        body = await request.json()
        result = await mcp_server.handle_request(body)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": {"code": -32603, "message": str(e)}}
        )


def main() -> None:
    """Run the server."""
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

