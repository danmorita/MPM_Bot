def get_data(simbolo, timeframe="M5", num_candles=500):
    import pandas as pd
    df = pd.DataFrame({
        "open": [], "high": [], "low": [], "close": [], "volume": []
    })
    return df
