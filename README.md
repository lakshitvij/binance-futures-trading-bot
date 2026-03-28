# Binance Futures Trading Bot

## About
This is a simple Python-based CLI trading bot that places orders on Binance Futures Testnet.  
I built this as part of an assignment to demonstrate API handling, clean code structure, and error handling.

## What it does
- Places MARKET and LIMIT orders  
- Supports both BUY and SELL  
- Takes input from command line  
- Shows clear order details after execution  
- Logs API requests, responses, and errors  

## Tech Used
- Python  
- python-binance  

## How to run

1. Install dependencies:
 pip install -r requirements.txt


2. Add your Binance Testnet API keys in:

bot/client.py


3. Run the bot:

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002


### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000


## Notes
- This uses Binance Futures Testnet (not real money)  
- Minimum order value should be above 100 USDT  

## Project Structure

bot/
cli.py
README.md
requirements.txt


## Status
Tested with both MARKET and LIMIT orders
