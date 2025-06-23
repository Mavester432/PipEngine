# strategy.py

def calculate_ema(prices, span):
    ema = []
    multiplier = 2 / (span + 1)
    for i, price in enumerate(prices):
        if i == 0:
            ema.append(price)
        else:
            ema.append((price - ema[-1]) * multiplier + ema[-1])
    return ema

def check_ema_crossover(candles):
    closes = [c["close"] for c in candles]

    if len(closes) < 21:
        return "hold"  # Not enough data

    short_ema = calculate_ema(closes, span=9)
    long_ema = calculate_ema(closes, span=21)

    # Check crossover
    if short_ema[-2] < long_ema[-2] and short_ema[-1] > long_ema[-1]:
        return "buy"
    elif short_ema[-2] > long_ema[-2] and short_ema[-1] < long_ema[-1]:
        return "sell"
    else:
        return "hold"
