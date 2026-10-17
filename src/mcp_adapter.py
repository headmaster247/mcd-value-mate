
class McDonaldsMCPAdapter:
    """
    Adapter boundary for official McDonald's MCP integration.

    Implement the actual tool calls only after verifying the
    connected server's tool names, schemas, and client SDK.
    """

    def __init__(self, client):
        self.client = client

    def list_tools(self):
        """Return the tools actually exposed by the MCP client."""
        return self.client.list_tools()

    def query_products(self, *args, **kwargs):
        """
        Placeholder for a verified read-only product query.

        Replace this method with the real MCP call after confirming
        the server's tool schema.
        """
        raise NotImplementedError(
            "Implement after verifying the official MCP tool schema."
        )
