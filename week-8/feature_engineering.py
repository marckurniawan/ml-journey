import numpy as np

def zscore_volume(df, threshold=2):
    rolling_mean = df["Volume"].rolling(window=20).mean()
    rolling_std = df["Volume"].rolling(window=20).std()
    df["Z-score"] = (df["Volume"] - rolling_mean) / rolling_std
    # std = df["Volume"].std()
    # df["Z-score"] = (df["Volume"] - df["Volume"].mean())/ std 
    # df["Volume_anomaly"] = (df["Z-score"] > 2) | (df["Z-score"] < -2)
    df["Volume_anomaly"]  = (df["Z-score"].abs() > threshold)
    df["Volume_BigEvent"] = (df["Z-score"].abs() > 3)

    return df


def ma_trend(df, fast=20, slow=50):
    sma_fast = df["Close"].rolling(window=fast).mean()
    sma_slow = df["Close"].rolling(window=slow).mean()
    diff = sma_fast - sma_slow
    
    df["trend"] = np.sign(diff)
    
    return df

def period_volatility(df, period=20):
    returns = df["Close"].pct_change()
    vol = returns.rolling(window=period).std()

    df["period_volatility"] = vol * np.sqrt(252)
    return df

    

def rate_of_change(df, period=5):
    # df["roc"]= (df["Close"] - df["Close"].shift(period)) / df["Close"].shift(period) * 100
    df["rate_of_change"] = df["Close"].pct_change(periods=period) * 100   
    return df

def near_psych_level(df, interval=500, tolerance=0.02):
    ratio = (df["Close"]/ interval).round()
    psychological_level = ratio * interval

    distance = np.abs(psychological_level - df["Close"])/psychological_level

    df["near_psych_level"] = distance <= tolerance

    return df

def label_making(df, horizon=5, threshold=0.015):
    df = df.copy()
    future_return = df["Close"].shift(-horizon) / df["Close"] -1
    df["target"] = np.where(
        future_return > threshold, 1,
        np.where(future_return < -threshold, -1, 0)
    )

    return df["target"]

def features(df):
    df = df.copy()

    df = zscore_volume(df)
    df = ma_trend(df)
    df = period_volatility(df)
    df = rate_of_change(df)
    df = near_psych_level(df)
    
    feature_cols = [
        "Z-score",
        "trend",
        "period_volatility",
        "rate_of_change",
        "near_psych_level"
    ]

    return df[feature_cols]

def buat_dataset(df):
    dataset = features(df)
    dataset["target"] = label_making(df)
    
    dataset = dataset.dropna()

    return dataset

import yfinance as yf

df = yf.download("BBCA.JK", period="2y")
df.columns = df.columns.droplevel("Ticker")

if __name__ == "__main__":
    dataset = buat_dataset(df)
    print(dataset.shape)
    print(dataset.head())
    print(dataset["target"].value_counts())