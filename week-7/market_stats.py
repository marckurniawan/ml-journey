import yfinance as yf
import pandas as pd
import numpy as np


def volatility(df, period=20):
    returns = df["Close"].pct_change().dropna()
    


    period_std = returns.rolling(window = period).std()
    latest_std = period_std.iloc[-1]
    returns_std = returns.std() 
    annualized_std = returns_std * np.sqrt(252)
    
    return {"latest_volatility" : latest_std,
            "annualized_volatility" : annualized_std,
            }

def volume_analysis(df, mode="konservatif"):
    thresholds = {
       "agresif" : 1,
       "konservatif": 2 
    }
    threshold = thresholds.get(mode, 2)
    
    volume = df["Volume"].replace([np.inf, -np.inf], np.nan).dropna()
    todays_volume = volume.iloc[-1]
    
    volume_mean = volume.mean()
    volume_std = volume.std()
    
    if todays_volume > volume_mean + threshold * volume_std:
        volume_status = "high"

    elif todays_volume < volume_mean - threshold * volume_std:
        volume_status = "low"

    else:
        volume_status = "normal"
    
    return {"volume_status": volume_status,
            "todays_volume" : todays_volume,
            "average_volume" : volume_mean,
            "volume_ratio" :  todays_volume / volume_mean
            }

# df = yf.download("BBCA.JK", period="1y")
# df.columns = df.columns.droplevel("Ticker")



# # print(f"Mean:     {returns.mean():.4f}")
# # # print(f"Std:      {returns.std():.4f}")
# # # print(f"Skewness: {returns.skew():.4f}")
# # # print(f"Kurtosis: {returns.kurtosis():.4f}")
# # threshold = returns.std() * 2
# # extreme = returns[returns.abs() > threshold]
# # print(f"Persen hari ekstrem: {len(extreme)/len(returns):.1%}")

# data = volatility(df)

# for key, value in data.items():
#     print(f"{key} : {value}")

# volume = volume_analysis(df, "agresif")

# for key, value in volume.items():
#     print(f"{key} : {value}")
