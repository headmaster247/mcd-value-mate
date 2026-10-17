# 麦麦精算师 · McValue Mate

An AI-powered meal planning Skill for McDonald's China.

## Project Overview

McValue Mate is an AI Skill designed to help users plan McDonald's meals according to their budget and preferences, using information returned by the official McDonald's China MCP tools.

## Features

- Budget-based meal recommendations.
- Meal combination and price comparison.
- Coupon information analysis when supported by the official tools.
- Nutritional information comparison when data is available.
- Alternative meal suggestions and budget calculations.

## Architecture

- Official McDonald's China MCP Server.
- AI Skill instructions and tool orchestration.
- Local meal filtering and budget calculations.
- Automated tests and usage examples.

## Requirements

A compatible AI client, an authorized MCP connection, and the runtime dependencies required by the implemented version.

## Setup

1. Configure the official MCP server using `mcp-config.example.json` as a reference.
2. Configure your authentication token securely.
3. Load `SKILL.md` in a compatible client.
4. Enter a budget and meal preferences.
5. Review the returned recommendations and their data sources.

## Security

Never commit real MCP tokens, passwords, or other credentials to this repository.

## Project Status

Initial development. Features will be marked as complete only after implementation and testing.

## Disclaimer

This is an independent community project and is not an official McDonald's product or endorsement.
