
# MCP Integration

## 1. Server Information

- Server: McDonald's China MCP Server
- Endpoint: `https://mcp.mcd.cn`
- Transport: Streamable HTTP
- Authentication: Bearer token

## 2. Available Tools

This section must be completed using the actual tools exposed by the connected MCP server.

| Tool Name | Purpose | Verification Status |
|---|---|---|
| To be verified | To be verified | Pending |
| To be verified | To be verified | Pending |

## 3. Integration Workflow

1. Receive the user's budget and meal preferences.
2. Query relevant information using the official MCP tools.
3. Validate the returned fields.
4. Calculate meal prices using verified data.
5. Filter and rank feasible combinations.
6. Return recommendations and explain data limitations.

## 4. Error Handling

Handle unavailable tools, failed requests, missing fields, invalid prices, and incomplete nutritional data without fabricating results.

## 5. Security

Authentication tokens must be stored securely and must never be committed to the public repository.

## 6. Testing Evidence

Record the actual tools tested, testing date, sanitized responses, and any limitations.

Do not mark tools as verified until real calls have succeeded.
