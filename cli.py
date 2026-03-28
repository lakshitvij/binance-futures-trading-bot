import argparse
from bot.client import BinanceClient
from bot.orders import create_order
from bot.validators import validate_input
from bot.logging_config import setup_logger
import logging

def main():
    setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        validate_input(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        client = BinanceClient()

        order = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("✅ Order placed successfully!")
        print(order)

        logging.info(f"Order success: {order}")

    except Exception as e:
        print("❌ Error:", str(e))
        logging.error(str(e))

if __name__ == "__main__":
    main()