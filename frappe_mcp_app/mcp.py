import frappe
import frappe_mcp

# Create MCP instance
mcp = frappe_mcp.MCP("frappe-mcp")

# Simple tool example
@mcp.tool()
def get_system_info():
    """Get basic system information."""
    return {
        "site": frappe.local.site,
        "user": frappe.session.user,
        "frappe_version": frappe.__version__
    }

# Register MCP endpoint
@mcp.register()
def handle_mcp():
    pass
