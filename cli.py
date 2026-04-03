import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        print("\n==============================")
        print("BINANCE TRADING BOT")
        print("==============================")

        print("\nStep 1: Validating input...")
        symbol, side, order_type, quantity, price = validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )
        print("Input validated successfully")

        print("\nStep 2: Connecting to Binance Testnet...")
        client = get_client()
        print("Connection established")

        print("\nStep 3: Order Request Summary")
        print("--------------------------------")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")
        print(f"Price    : {price}")

        confirm = input("\nConfirm order? (yes/no): ")
        if confirm.lower() != "yes":
            print("Order cancelled by user")
            return

        print("\nStep 4: Placing order...")
        order = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\nStep 5: Order Result")
        print("--------------------------------")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")

        print("\nProcess completed successfully")

    except Exception as e:
        print("\nError:", str(e))


if __name__ == "__main__":
    main()