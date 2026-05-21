import pandas as pd
import yfinance as yf
from pandas_basics import analisis_saham, deteksi_anomali_volume, cek_harga_psikologis



def main():
    stock = input("Stock: ").upper() + ".JK"
    print(stock)
    df = yf.download(stock, period="1y")
    df.columns = df.columns.droplevel("Ticker")
    data = analisis_saham(df)

    anomaly = deteksi_anomali_volume(df)
    anomaly_price = anomaly["Close"]
    print("\n=== Ringkasan Saham ===")
    for key, value in data.items():
        print(f"{key}: {value}")
    for harga in anomaly_price:
        key_level = cek_harga_psikologis(harga)

        print(
            f"{harga} → "
            f"level: {key_level['psychological_level']}, "
            f"jarak: {key_level['distance_percent']:.1%}, "
            f"dekat: {key_level['within_tolerance']}"
        )



if __name__ == "__main__":
    main()