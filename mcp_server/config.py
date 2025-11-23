"""Configuration management for the MCP server."""

import os
from typing import Final

from dotenv import load_dotenv

from .utils.errors import ConfigError

# Load environment variables from .env file
load_dotenv()

# ATTOM API Configuration
ATTOM_API_KEY: Final[str] = os.getenv("ATTOM_API_KEY", "")
BASE_ATTOM_URL: Final[str] = os.getenv(
    "BASE_ATTOM_URL", "https://api.gateway.attomdata.com/propertyapi/v1.0.0"
)


def validate_config() -> None:
    """Validate that required configuration is present."""
    if not ATTOM_API_KEY:
        raise ConfigError(
            "ATTOM_API_KEY is required. Set it in your .env file or environment variables."
        )

