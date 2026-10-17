# McValue Mate

## Purpose

Help users plan McDonald's China meals within a specified budget using verified information from connected official MCP tools.

## When to Use

Use this Skill when users want to compare meal options, plan a budget, review available coupon information, or compare available nutritional information.

## Workflow

1. Ask for the user's budget and preferences when needed.
2. Inspect the actual tools available through the MCP connection.
3. Query relevant official information.
4. Validate the returned data.
5. Calculate meal totals using available prices.
6. Filter combinations that exceed the budget.
7. Rank feasible options based on the user's preferences.
8. Explain recommendations, price differences, and missing information.

## Data Integrity

- Never invent products, prices, coupons, or nutritional values.
- Do not assume a tool exists before verifying its schema.
- Do not treat missing prices as zero.
- Clearly label incomplete or unavailable information.

## Safety

- Never expose authentication tokens.
- Do not place orders, make payments, or claim coupons without explicit authorization and confirmation.
- Prefer read-only tools for the initial implementation.

## Output

Provide item names, quantities, verified prices, total cost, remaining budget, nutritional information when available, and an explanation of the recommendation.

## Fallback

If official data is unavailable, explain the limitation and do not present mock data as real official information.
