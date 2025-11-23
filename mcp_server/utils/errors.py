"""Custom exceptions for the MCP server."""


class APIError(Exception):
    """Base exception for API-related errors."""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class ConfigError(Exception):
    """Exception raised when configuration is invalid or missing."""

    pass

