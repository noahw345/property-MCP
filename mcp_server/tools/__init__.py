"""MCP Tools Package."""

from mcp.server.fastmcp import FastMCP

from .comparables_tool import get_comparables
from .property_info_tool import get_property_info


def register_tools(mcp: FastMCP) -> None:
    """Register all tools with the FastMCP server."""
    mcp.tool(
        name="get_property_info",
        description="Fetch property details from ATTOM given a full address.",
    )(get_property_info)
    
    mcp.tool(
        name="get_comparables",
        description="Fetch 3 comparable properties for a given address from ATTOM.",
    )(get_comparables)


__all__ = ["get_property_info", "get_comparables", "register_tools"]

