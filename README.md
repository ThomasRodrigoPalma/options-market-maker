# Options Market Maker

## What
A market maker continuously quotes a price to buy (bid) and a price to sell (ask), and earns the small gap between them (the spread) while managing the risk of the positions it ends up holding.
I'm building a simple options market maker on Deribit (BTC options) from scratch, to learn trading, quantitative finance and systems programming by actually doing it.

## Stack
- Python: data collection, pricing, simulation
- SQL (SQLite): storing market data
- C/C++: fast pricing engine
- Git/GitHub: version control

## Roadmap
0. Setup: tools, Git, GitHub
1. Data: collect Deribit option quotes into SQLite
2. Pricing: Black-Scholes, implied volatility, Greeks
3. Simulator: replay recorded data, fills, P&L
4. Strategy + risk: quoting, delta hedging, risk limits
5. Speed: rewrite the pricer in C/C++
6. Paper trading on Deribit testnet
7. Write-up: results and lessons

## Status
Phase 0 done, starting Phase 1 (Data).