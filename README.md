# Frappe MCP App

Minimal Frappe app with MCP integration.

## Installation

```bash
bench get-app https://github.com/chinmaybhatk/frappe-mcp-app.git
bench --site your-site install-app frappe_mcp_app
```

## MCP Endpoint

Once installed, your MCP server will be available at:
```
https://your-site/api/method/frappe_mcp_app.mcp.handle_mcp
```

## Usage

Test with MCP Inspector or any MCP-compatible client.
