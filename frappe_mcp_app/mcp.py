import frappe_mcp
import frappe
from typing import Dict, Any, List, Optional

# Create MCP server instance
mcp = frappe_mcp.MCP("frappe-mcp-server")

# Tool 1: Get ToDo items
@mcp.tool()
def get_todos(status: Optional[str] = None, limit: int = 20):
    """Get ToDo items for the current user.
    
    Args:
        status: Filter by status (Open, Closed, Cancelled). If not provided, returns all.
        limit: Maximum number of items to return.
    """
    filters = {"owner": frappe.session.user}
    if status:
        filters["status"] = status
    
    todos = frappe.get_all(
        "ToDo",
        filters=filters,
        fields=["name", "description", "status", "priority", "date", "allocated_to"],
        limit=limit,
        order_by="modified desc"
    )
    
    return {
        "success": True,
        "count": len(todos),
        "todos": todos
    }

# Tool 2: Create ToDo
@mcp.tool()
def create_todo(description: str, priority: str = "Medium", date: Optional[str] = None, allocated_to: Optional[str] = None):
    """Create a new ToDo item.
    
    Args:
        description: Description of the ToDo item.
        priority: Priority level (Low, Medium, High, Urgent).
        date: Due date in YYYY-MM-DD format.
        allocated_to: Email of the user to assign to.
    """
    try:
        todo = frappe.get_doc({
            "doctype": "ToDo",
            "description": description,
            "priority": priority,
            "status": "Open",
            "date": date,
            "allocated_to": allocated_to or frappe.session.user,
            "assigned_by": frappe.session.user
        })
        todo.insert()
        
        return {
            "success": True,
            "message": f"ToDo created successfully",
            "todo": {
                "name": todo.name,
                "description": todo.description,
                "status": todo.status
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Tool 3: List documents from any DocType
@mcp.tool()
def get_doctype_list(doctype: str, filters: Optional[Dict[str, Any]] = None, limit: int = 20, fields: Optional[List[str]] = None):
    """Get a list of documents from any DocType.
    
    Args:
        doctype: Name of the DocType (e.g., Customer, Item, Sales Invoice).
        filters: Optional filters as key-value pairs.
        limit: Maximum number of documents to return.
        fields: List of fields to return. If not specified, returns name and common fields.
    """
    try:
        if not fields:
            # Default fields based on common patterns
            fields = ["name", "modified", "owner"]
            
            # Add doctype-specific fields
            if doctype == "Customer":
                fields.extend(["customer_name", "customer_group", "territory"])
            elif doctype == "Item":
                fields.extend(["item_name", "item_group", "stock_uom"])
            elif doctype == "Sales Invoice":
                fields.extend(["customer", "posting_date", "grand_total", "status"])
        
        docs = frappe.get_all(
            doctype,
            filters=filters or {},
            fields=fields,
            limit=limit,
            order_by="modified desc"
        )
        
        return {
            "success": True,
            "doctype": doctype,
            "count": len(docs),
            "documents": docs
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Error fetching {doctype} list"
        }

# Tool 4: Get document details
@mcp.tool()
def get_document(doctype: str, name: str):
    """Get details of a specific document.
    
    Args:
        doctype: Name of the DocType.
        name: Name/ID of the document.
    """
    try:
        doc = frappe.get_doc(doctype, name)
        
        # Check permissions
        if not doc.has_permission("read"):
            return {
                "success": False,
                "error": "Insufficient permissions to read this document"
            }
        
        return {
            "success": True,
            "document": doc.as_dict()
        }
    except frappe.DoesNotExistError:
        return {
            "success": False,
            "error": f"{doctype} '{name}' not found"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Tool 5: Create a document
@mcp.tool()
def create_document(doctype: str, data: Dict[str, Any]):
    """Create a new document of any DocType.
    
    Args:
        doctype: Name of the DocType to create.
        data: Dictionary containing field values for the document.
    """
    try:
        doc = frappe.get_doc({
            "doctype": doctype,
            **data
        })
        doc.insert()
        
        return {
            "success": True,
            "message": f"{doctype} created successfully",
            "document": {
                "name": doc.name,
                "doctype": doctype
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Error creating {doctype}"
        }

# Register the MCP endpoint
@mcp.register()
def handle_mcp():
    """Entry point for MCP requests.
    
    This endpoint will be available at:
    /api/method/frappe_mcp_app.mcp.handle_mcp
    """
    # All tools are already registered via decorators
    pass
