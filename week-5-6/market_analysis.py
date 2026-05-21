import pandas as pd
import yfinance as yf
from pandas_basics import analisis_saham, deteksi_anomali_volume, cek_harga_psikologis

def cek_tren(df, fast=20, slow=50):
    df = df.copy()
    SMA_20 = df["Close"].rolling(window=fast).mean()
    SMA_50 = df["Close"].rolling(window=slow).mean()

    if SMA_20.iloc[-1] < SMA_50.iloc[-1]:
        return "Downtrend"
    elif SMA_20.iloc[-1] > SMA_50.iloc[-1]:
        return "Uptrend"
    else:
        return "Neutral"
    

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