"""ATTOM Data API client."""

import requests
from typing import Any

from ..config import ATTOM_API_KEY, BASE_ATTOM_URL, validate_config
from ..utils.errors import APIError


class ATTOMClient:
    """Client for interacting with the ATTOM Data API."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None):
        """Initialize the ATTOM client.

        Args:
            api_key: ATTOM API key. Defaults to config value.
            base_url: Base URL for ATTOM API. Defaults to config value.
        """
        # Validate config when client is instantiated
        validate_config()
        
        self.api_key = api_key or ATTOM_API_KEY
        self.base_url = base_url or BASE_ATTOM_URL
        self.session = requests.Session()
        self.session.headers.update(
            {
                "apikey": self.api_key,
                "Accept": "application/json",
            }
        )

    def get_property_info(self, address: str) -> dict[str, Any]:
        """Fetch property information for a given address.

        Args:
            address: Full property address (e.g., "123 Main St, City, State ZIP").

        Returns:
            Dictionary containing property information from ATTOM API.

        Raises:
            APIError: If the API request fails or returns an error.
        """
        url = f"{self.base_url}/property/address"
        params = {"address": address}

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response else None
            error_msg = f"ATTOM API error: {e}"
            if e.response:
                try:
                    error_data = e.response.json()
                    error_msg = error_data.get("error", {}).get(
                        "message", error_msg
                    )
                except ValueError:
                    error_msg = e.response.text or error_msg
            raise APIError(error_msg, status_code=status_code) from e
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {e}") from e

    def get_comparables(self, address: str, count: int = 3) -> dict[str, Any]:
        """Fetch comparable properties for a given address.

        Args:
            address: Full property address (e.g., "123 Main St, City, State ZIP").
            count: Number of comparables to return. Defaults to 3.

        Returns:
            Dictionary containing comparable properties from ATTOM API.

        Raises:
            APIError: If the API request fails or returns an error.
        """
        url = f"{self.base_url}/property/comps"
        params = {"address": address, "count": count}

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response else None
            error_msg = f"ATTOM API error: {e}"
            if e.response:
                try:
                    error_data = e.response.json()
                    error_msg = error_data.get("error", {}).get(
                        "message", error_msg
                    )
                except ValueError:
                    error_msg = e.response.text or error_msg
            raise APIError(error_msg, status_code=status_code) from e
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {e}") from e

