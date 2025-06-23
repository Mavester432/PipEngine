# data.py

import requests
from config import OANDA_API_URL, ACCESS_TOKEN, INSTRUMENT, GRANULARITY

def fetch_candles(count=50):
    endpoint = f"/instruments/{INSTRUMENT}/candles"
    url = f"{OANDA_API_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    params = {
        "granularity": GRANULARITY,
        "count": count,
        "price": "M"  # Midpoint candles
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error fetching candles: {response.status_code} - {response.text}")
        return []

    data = response.json()["candles"]

    # Convert and return cleaned candle data
    candles = [{
        "time": c["time"],
        "open": float(c["mid"]["o"]),
        "high": float(c["mid"]["h"]),
        "low": float(c["mid"]["l"]),
        "close": float(c["mid"]["c"]),
        "volume": c["volume"]
    } for c in data if c["complete"]]

    return candles
