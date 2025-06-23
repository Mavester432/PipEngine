# executor.py

from config import ACCOUNT_ID, TRADE_UNITS
from auth import make_request

def place_order(direction):
    if direction not in ["buy", "sell"]:
        print("No valid signal to trade.")
        return

    print(f"🔔 EXECUTING {direction.upper()} ORDER")

    order_data = {
        "order": {
            "units": str(TRADE_UNITS if direction == "buy" else -TRADE_UNITS),
            "instrument": "EUR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
        }
    }

    # Simulated output
    print("📄 Order payload:")
    print(order_data)

    # Uncomment below if ready to go live
    # response = make_request("POST", f"/accounts/{ACCOUNT_ID}/orders", data=order_data)
    # print("📬 Response:", response)
