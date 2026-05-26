def generate_signal(trend, trend_confirmed, volume_status, price_direction):
    """
    Generate trading signal berdasarkan kombinasi indikator.
    Return: "BUY", "SELL", atau "NEUTRAL"
    """
    if trend == "bullish" and trend_confirmed == "bullish" and volume_status == "high" and price_direction == "up":
        return "buy"
    elif trend == "bearish" and trend_confirmed == "bearish" and volume_status == "high" and price_direction == "down":
        return "sell"
    else:
        return "neutral"
    
