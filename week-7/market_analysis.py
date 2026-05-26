import pandas as pd
import yfinance as yf
from pandas_basics import analisis_saham, deteksi_anomali_volume, cek_harga_psikologis

def cek_tren(df, fast=20, slow=50):
    df = df.copy()
    sma_20 = df["Close"].rolling(window=fast).mean()
    sma_50 = df["Close"].rolling(window=slow).mean()

    if sma_20.iloc[-1] > sma_50.iloc[-1]:
        return "bullish"
    elif sma_20.iloc[-1] < sma_50.iloc[-1]:
        return "bearish"
    else:
        return "neutral"
    

def cek_trend_confirmed(df, period=5, ma_window=20):
    """
    Validasi tren dengan scoring konsistensi N hari terakhir.
    Return: "bullish", "bearish", atau "neutral"
    """
    sma_20 = df["Close"].rolling(window=ma_window).mean()
    sma_5 = df["Close"].rolling(window=period).mean()

    score = 0

    for i in range(-1, -period-1, -1):
        if sma_5.iloc[i] > sma_20.iloc[i]:
            score+=1
        elif sma_5.iloc[i] < sma_20.iloc[i]:
            score-=1
        else:
            continue
    if score > 2:
        return "bullish"
    elif score < -2:
        return "bearish"
    else:
        return "neutral"    

def main():
    stock = input("Stock: ").upper() + ".JK"
    print(stock)
    df = yf.download(stock, period="1y")
    df.columns = df.columns.droplevel("Ticker")
    data = analisis_saham(df)

    anomaly = deteksi_anomali_volume(df)

    print("\n=== Ringkasan Saham ===")
    for key, value in data.items():
        print(f"{key}: {value}")
    for index, row in anomaly.iterrows():

        harga = row["Close"]

        key_level = cek_harga_psikologis(harga)

        print(
            
            f"harga: {harga:.2f} → "
            f"level: {key_level['psychological_level']}, "
            f"jarak: {key_level['distance_percent']:.1%}, "
            f"dekat: {key_level['within_tolerance']}, "
            f"arah: {row['price_direction']}"
        )
    print(f"Trend: {cek_tren(df)}")


if __name__ == "__main__":
    main()