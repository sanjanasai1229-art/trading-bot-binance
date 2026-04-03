# Trading Bot – Binance Futures Testnet

## Overview

This project is a simplified trading bot built in Python that interacts with the Binance Futures Testnet (USDT-M). It supports placing MARKET and LIMIT orders via a command-line interface (CLI), with proper logging, validation, and error handling.

---

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL sides
* CLI-based input using argparse
* Input validation for all parameters
* Structured and modular code design
* Logging of API requests, responses, and errors
* Graceful error handling (no crashes)

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py        # Binance client wrapper
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   ├── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
├── bot.log              # Log file (generated after execution)
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create Virtual Environment

```
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## How to Run

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 30000
```

---

## Sample Output

```
Validating input...
Connecting to Binance Testnet...

Order Request Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.01}

Placing order...

Order Result:
{'orderId': 'FAILED', 'status': 'ERROR', 'executedQty': 0, 'avgPrice': 0}
```

---

## Logging

All API interactions are logged in:

```
bot.log
```

Includes:

* Order requests
* API responses
* Errors (if any)

---

## Note on API Keys

While implementing the project, Binance Futures Testnet required identity verification (KYC) for API key generation, which restricted direct order execution.

To ensure uninterrupted development and demonstrate system design, the application:
- Uses correct Binance Futures API endpoints
- Handles API failures gracefully
- Returns structured responses even in failure scenarios

This reflects real-world robustness where external API constraints must be handled without breaking the system.

---

## Assumptions

* Testnet API may not execute real trades without valid credentials
* Focus is on structure, validation, and error handling

---

## Future Improvements

* Add Stop-Limit / OCO orders
* Improve CLI UX with prompts
* Add simple UI dashboard

---

## Author

Sanjana Sai Tangudu
