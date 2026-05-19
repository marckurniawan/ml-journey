import yfinance as yf
import pandas as pd


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
df = yf.download("BBCA.JK", period="1y")
df.columns = df.columns.droplevel("Ticker")

hasil = analisis_saham(df)
for k, v in hasil.items():
    print(f"{k}: {v}")