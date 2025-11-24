"""MCP tool for fetching property information."""

from typing import Any

from ..services.attom_client import ATTOMClient
from ..utils.errors import APIError

# Lazy initialization of ATTOM client
_attom_client: ATTOMClient | None = None


def _get_client() -> ATTOMClient:
    """Get or create ATTOM client instance."""
    global _attom_client
    if _attom_client is None:
        _attom_client = ATTOMClient()
    return _attom_client


def get_property_info(address: str) -> dict[str, Any]:
    """Fetch property information for a given address.

    Args:
        address: Full property address.

    Returns:
        Dictionary containing property information from ATTOM API.

    Raises:
        APIError: If the API request fails.
    """
    try:
        client = _get_client()
        return client.get_property_info(address)
    except APIError as e:
        error_response: dict[str, Any] = {
            "error": True,
            "message": e.message,
        }
        if e.status_code:
            error_response["status_code"] = e.status_code
        return error_response

