import yfinance as yf
from market_analysis import (cek_tren, cek_trend_confirmed)
from market_stats import (volatility, volume_analysis)
from trading_signal import generate_signal
from pandas_basics import (analisis_saham, deteksi_anomali_volume, cek_harga_psikologis)


def main():
    ticker = input("Please enter the ticker:").lower() + ".JK"
    df = yf.download(ticker, period= "1y")
    df.columns = df.columns.droplevel("Ticker")
    basic_data = analisis_saham(df)


    trend = cek_tren(df)    

    confirmed_trend = cek_trend_confirmed(df)

    
    volatility_data = volatility(df)

    
    volume_data = volume_analysis(df)

    anomaly = deteksi_anomali_volume(df)

    latest_return = df["Close"].pct_change().iloc[-1]

    if latest_return > 0:
        price_direction = "up"

    elif latest_return < 0:
        price_direction = "down"

    else:
        price_direction = "neutral"

    signal = generate_signal(
        trend,
        confirmed_trend,
        volume_data["volume_status"],
        price_direction
    )

    print("\n=== BASIC ANALYSIS ===")

    for key, value in basic_data.items():
        print(f"{key}: {value}")

    print("\n=== MARKET ANALYSIS ===")

    print(f"Trend: {trend}")

    print(f"Confirmed Trend: {confirmed_trend}")

    print(
        f"Annualized Volatility: "
        f"{volatility_data['annualized_volatility']:.2%}"
    )

    print(f"Volume Status: {volume_data['volume_status']}")

    

    print(f"Trading Signal: {signal}")

    print("\n=== VOLUME ANOMALY ===")

    for index, row in anomaly.iterrows():

        harga = row["Close"]

        key_level = cek_harga_psikologis(harga)

        print(
            f"{index.date()} | "
            f"Harga: {harga:.2f} | "
            f"Level: {key_level['psychological_level']} | "
            f"Distance: {key_level['distance_percent']:.1%} | "
            f"Near: {key_level['within_tolerance']} | "
            f"Direction: {row['price_direction']}"
        )


if __name__ == "__main__":
    main()
