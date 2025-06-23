# bot.py

import time
from data import fetch_candles
from strategy import check_ema_crossover
from executor import place_order

def run_bot():
    print("🤖 PipEngine started...\n")

    while True:
        print("🔄 Checking market conditions...")

        candles = fetch_candles()
        if not candles:
            print("❌ Failed to fetch candles.\n")
            time.sleep(60)
            continue

        signal = check_ema_crossover(candles)
        print(f"📊 Signal: {signal.upper()}")

        place_order(signal)

        print("⏳ Sleeping for 5 minutes...\n")
        time.sleep(300)  # Sleep for 5 minutes

if __name__ == "__main__":
    run_bot()
