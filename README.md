# Property MCP Server

A production-grade Model Context Protocol (MCP) server for property data retrieval using the ATTOM Data API.

## Features

- **Clean Architecture**: Modular, extensible structure for adding new tools
- **Type Safety**: Strong typing throughout the codebase
- **Error Handling**: Comprehensive error handling with custom exceptions
- **Configuration Management**: Centralized config with environment variable support
- **FastAPI Integration**: Modern async web framework for hosting the MCP server

## Project Structure

```
mcp_server/
├── server.py               # Entrypoint running FastAPI + MCP
├── config.py               # ATTOM keys + environment loading
├── tools/
│   ├── __init__.py
│   └── property_tools.py   # get_property_info tool
├── services/
│   ├── __init__.py
│   └── attom_client.py     # ATTOM HTTP client wrapper
├── utils/
│   ├── __init__.py
│   └── errors.py           # custom exceptions
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Configuration

1. **Create a `.env` file** in the project root:
```bash
ATTOM_API_KEY=your_attom_api_key_here
BASE_ATTOM_URL=https://api.gateway.attomdata.com/propertyapi/v1.0.0
```

2. **Set your ATTOM API key**:
   - Get your API key from [ATTOM Data Solutions](https://www.attomdata.com/)
   - Add it to the `.env` file as shown above
   - Alternatively, set it as an environment variable: `export ATTOM_API_KEY=your_key`

## Running the Server

Start the server:
```bash
python -m mcp_server.server
```

Or using uvicorn directly:
```bash
uvicorn mcp_server.server:app --host 0.0.0.0 --port 8000
```

The server will start on `http://0.0.0.0:8000`.

## API Endpoints

### Health Check
```bash
GET /
```

Response:
```json
{
  "status": "healthy",
  "service": "property-mcp-server"
}
```

### MCP Endpoint
```bash
POST /mcp
```

## MCP Tools

### `get_property_info`

Fetches property details from ATTOM given a full address.

**Parameters:**
- `address` (string): Full property address (e.g., "123 Main St, City, State ZIP")

**Example MCP Tool Call JSON:**

```json
{
  "method": "tools/call",
  "params": {
    "name": "get_property_info",
    "arguments": {
      "address": "123 Main St, Los Angeles, CA 90001"
    }
  }
}
```

**Example Response:**

```json
{
  "property": {
    "address": {
      "oneLine": "123 Main St, Los Angeles, CA 90001",
      "city": "Los Angeles",
      "state": "CA",
      "zip": "90001"
    },
    "assessment": {
      "taxAmount": 5000,
      "marketValue": 500000
    }
  }
}
```

**Error Response:**

```json
{
  "error": true,
  "message": "ATTOM API error: Invalid address",
  "status_code": 400
}
```

### `get_comparables`

Fetches 3 comparable properties for a given address from ATTOM.

**Parameters:**
- `address` (string): Full property address (e.g., "123 Main St, City, State ZIP")

**Example MCP Tool Call JSON:**

```json
{
  "method": "tools/call",
  "params": {
    "name": "get_comparables",
    "arguments": {
      "address": "123 Main St, Los Angeles, CA 90001"
    }
  }
}
```

**Example Response:**

```json
{
  "comparables": [
    {
      "address": {
        "oneLine": "125 Main St, Los Angeles, CA 90001",
        "city": "Los Angeles",
        "state": "CA",
        "zip": "90001"
      },
      "assessment": {
        "marketValue": 495000
      }
    },
    {
      "address": {
        "oneLine": "121 Main St, Los Angeles, CA 90001",
        "city": "Los Angeles",
        "state": "CA",
        "zip": "90001"
      },
      "assessment": {
        "marketValue": 510000
      }
    },
    {
      "address": {
        "oneLine": "127 Main St, Los Angeles, CA 90001",
        "city": "Los Angeles",
        "state": "CA",
        "zip": "90001"
      },
      "assessment": {
        "marketValue": 505000
      }
    }
  ]
}
```

**Error Response:**

```json
{
  "error": true,
  "message": "ATTOM API error: Invalid address",
  "status_code": 400
}
```

## Extending the Server

To add new tools:

1. **Create a new tool file** in `tools/` (e.g., `tools/comps_tools.py`)
2. **Define your tool** using the `@tool` decorator:
```python
from mcp import Argument, tool

@tool(
    name="get_comps",
    description="Get comparable properties",
    args=[Argument(name="address", type="string")]
)
def get_comps(address: str) -> dict:
    # Your implementation
    pass
```

3. **Export it** in `tools/__init__.py`
4. **Register it** in `server.py`:
```python
from .tools import get_comps
mcp_server.add_tool(get_comps)
```

## Error Handling

The server includes custom exceptions:

- `APIError`: Raised for API-related errors (includes status code)
- `ConfigError`: Raised when configuration is invalid or missing

All errors are caught and returned as structured JSON responses.

## Development

### Code Style

- Follow PEP 8 guidelines
- Use type hints throughout
- Write clear, concise, and clean code

### Testing

(Add your testing instructions here)

## License

(Add your license information here)

## Support

For issues or questions, please open an issue in the repository.

