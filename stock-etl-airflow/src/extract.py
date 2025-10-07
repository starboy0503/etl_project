import yfinance as yf
import pandas as pd
from config import TICKERS,YF_PERIOD,YF_INTERVAL


def extract_ticker(ticker,period=YF_PERIOD,interval=YF_INTERVAL):
    """
    Returns a DataFrame with columns:
    ['Open','High','Low','Close','Adj Close','Volume'] indexed by DatetimeIndex
    """

    df=yf.download(tickers=ticker,period=period,interval=interval,progress=False,threads=False)
    if df.empty:
        return pd.DataFrame()
    df=df.reset_index().rename(columns={
        "Open":"open",
        "High":"high",
        "Low":"low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume",
        "Date": "dt",
        "Datetime": "dt"
    })

    if "dt" not in df.columns:
        df["dt"]=df.index
    
    df["ticker"]=ticker

    cols=["ticker","dt","open","high","low","close","adj_close", "volume"]
    return df[cols]

def extract_all(tickers=TICKERS,period=YF_PERIOD,interval=YF_INTERVAL):
    dfs=[]
    for t in tickers:
        try:
            df=extract_ticker(t,period,interval)
            if not df.empty:
                dfs.append(df)
        except Exception as e:
            print(f"extract error {t}: {e}")
    if dfs:
        return pd.concat(dfs,ignore_index=True)
    return None
