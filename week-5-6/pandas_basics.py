import yfinance as yf
import pandas as pd
import numpy as np

def analisis_saham(df):
    """
    Menerima DataFrame yfinance.
    Return dict berisi ringkasan lengkap.
    """
    daily_return = df["Close"].pct_change()
    std = daily_return.std()
    datas ={
        "mean" :df["Close"].mean(),
        "mean_volume" :df["Volume"].mean(),
        "max" :df["Close"].max(),
        "min" :df["Close"].min(),
        "std" :std,
        "Harga_tertinggi" : df["Close"].idxmax(),
        "Harga_terendah" : df["Close"].idxmin(),
        "volatile" : std > 0.02
    }
    
    return datas

def deteksi_anomali_volume(df, threshold=2):
   
    std = df["Volume"].std()
    df["Z-score"] = (df["Volume"] - df["Volume"].mean())/ std 
    # df["Volume_anomaly"] = (df["Z-score"] > 2) | (df["Z-score"] < -2)
    df["Volume_anomaly"]  = (df["Z-score"].abs() > threshold)
    df["Volume_BigEvent"] = (df["Z-score"].abs() > 3)
    df["Daily_Return"] = df["Close"].pct_change()
    df["price_direction"] = np.where(
        df["Daily_Return"] >= 0,
        "up",
        "down"
    )

    return df[df["Volume_anomaly"]]
    

def cek_harga_psikologis(harga, interval=500, tolerance=0.02):
    """
    Cek apakah harga mendekati level psikologis.
    Level psikologis: kelipatan interval (500, 1000, 1500, dst)
    Return dict: level terdekat dan apakah dalam tolerance.
    """
    ratio = round(harga/ interval)
    psychological_level = ratio * interval
    distance = abs(psychological_level - harga)/psychological_level
    near = distance <= tolerance
    data = {
    "harga": harga,
    "psychological_level": psychological_level,
    "distance_percent": distance,
    "within_tolerance": near
    }

    return data
# Download data BBCA 1 tahun terakhir
# df = yf.download("BBCA.JK", period="1y")
# # print(df.head())
# # print(df.shape)
# # print(df.dtypes)
# df.columns = df.columns.droplevel("Ticker")


# print(df["Close"].max())
# print(df["Close"].min())
# print(df["Volume"].mean())
# print(df["Close"].idxmax())
# df = yf.download("BBCA.JK", period="1y")
# df.columns = df.columns.droplevel("Ticker")

# hasil = analisis_saham(df)
# for k, v in hasil.items():
#     print(f"{k}: {v}")
# import yfinance as yf


# df = yf.download("BBCA.JK", period="1y")
# df.columns = df.columns.droplevel("Ticker")

# anomali = deteksi_anomali_volume(df)
# print(f"Jumlah hari anomali: {len(anomali)}")
# print(anomali[["Close", "Volume", "Z-score"]].to_string())

# harga_anomali = anomali["Close"]

# for harga in harga_anomali:
#     hasil = cek_harga_psikologis(harga)
#     print(f"{harga} → level: {hasil['psychological_level']}, "
#           f"jarak: {hasil['distance_percent']:.1%}, "
#           f"dekat: {hasil['within_tolerance']}")

# tickers = ["BBCA.JK", "BMRI.JK", "TLKM.JK"]
# df = yf.download(tickers, period="1y")

# # print(df.head())
# # print(df.columns)
# close_df = df["Close"]
# print(close_df.pct_change())
# print(close_df.corr())