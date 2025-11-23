"""MCP tool for fetching property information."""

from typing import Any

from ..services.attom_client import ATTOMClient
from ..utils.errors import APIError

# Initialize ATTOM client instance
_attom_client = ATTOMClient()


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
        return _attom_client.get_property_info(address)
    except APIError as e:
        error_response: dict[str, Any] = {
            "error": True,
            "message": e.message,
        }
        if e.status_code:
            error_response["status_code"] = e.status_code
        return error_response

