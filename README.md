# a1-cost-tracker

Assignment 1 for the Agentic AI cohort: a small tool that works out what an AI model API call costs from its token usage.

## How it works

`main.py` has a `cost(tokens, price_per_million)` function. Providers price tokens per 1 million, so the function multiplies the tokens by the price and divides by 1,000,000. It runs on example numbers for now. Real token counts from the Gemini and Groq APIs will replace them.

## Run

    uv run main.py

## Sample output

    Cost per call: $0.000935

## Acknowledgements

I wrote the code myself. Claude (Anthropic) helped me understand the per-million pricing logic, specifically why the cost is divided by 1,000,000.
