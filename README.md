# Property MCP Server

A minimal Model Context Protocol server that connects Claude AI to real estate data via the ATTOM Data API.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up .env file
echo "ATTOM_API_KEY=your_key_here" > .env

# Test the tool
python test_tool.py "1600 Amphitheatre Parkway, Mountain View, CA 94043"

# Run the server (for Claude Desktop)
python -m mcp_server.server
```

## Architecture

```
mcp_server/
├── server.py            # Entry point
├── tools/
│   └── property_info_tool.py  # tool interface
├── services/
│   └── attom_client.py  # HTTP client
├── config.py            # Environment config
└── utils/
    └── errors.py        # Exceptions
```
## Design Decisions

1. **Clean Separation**: Tool → Service → API layers
2. **Error Handling**: API errors returned as structured responses
3. **Minimal Dependencies**: Only `mcp`, `requests`, `python-dotenv`

## Error Handling

Errors are caught and returned as structured JSON responses:

```python
{
  "error": True,
  "message": "ATTOM API error: 400 Bad Request",
  "status_code": 400
}
```

- **API errors**: HTTP errors parsed from ATTOM API responses
- **Network errors**: Connection failures wrapped in APIError
- **Config errors**: Missing API key raises ConfigError at startup
- **Tool layer**: Catches APIError and returns error dict (never raises)

## Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "property-mcp": {
      "command": "/path/to/venv/bin/python3.12",
      "args": ["-m", "mcp_server.server"],
      "cwd": "/path/to/property-MCP",
      "env": {
        "PYTHONPATH": "/path/to/property-MCP"
      }
    }
  }
}
```
