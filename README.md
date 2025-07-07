# Frappe MCP App

A Frappe app that exposes tools to AI assistants using the Model Context Protocol (MCP).

## Features

- Get ToDo items
- Create ToDo items
- List documents from any DocType
- Get document details
- Create documents

## Installation

1. Add this app to your Frappe bench:
```bash
bench get-app https://github.com/chinmaybhatk/frappe-mcp-app.git
```

2. Install on your site:
```bash
bench --site your-site install-app frappe_mcp_app
```

## MCP Endpoint

Once installed, your MCP server will be available at:
```
https://your-site/api/method/frappe_mcp_app.mcp.handle_mcp
```

## Testing

Use the MCP Inspector or any MCP-compatible client to test the endpoint.

## Available Tools

- `get_todos`: Get all ToDo items for the current user
- `create_todo`: Create a new ToDo item
- `get_doctype_list`: List documents from any DocType
- `get_document`: Get details of a specific document
- `create_document`: Create a new document

## License

MIT