"""MCP tool for fetching comparable properties."""

from typing import Any

from ..services.attom_client import ATTOMClient
from ..utils.errors import APIError

# Initialize ATTOM client instance
_attom_client = ATTOMClient()


def get_comparables(address: str) -> dict[str, Any]:
    """Fetch comparable properties for a given address.

    Args:
        address: Full property address.

    Returns:
        Dictionary containing comparable properties from ATTOM API.

    Raises:
        APIError: If the API request fails.
    """
    try:
        return _attom_client.get_comparables(address, count=3)
    except APIError as e:
        error_response: dict[str, Any] = {
            "error": True,
            "message": e.message,
        }
        if e.status_code:
            error_response["status_code"] = e.status_code
        return error_response

