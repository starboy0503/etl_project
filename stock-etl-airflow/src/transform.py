import pandas as pd

def compute_indicators(df):
    """
    Expects df with columns: ['ticker','dt','open','high','low','close','adj_close','volume']
    Returns df with new columns: sma_5, sma_20, daily_return
    """

    df=df.copy()
    df["dt"]=pd.to_datetime(df["dt"])
    df["dt_iso"]=df["dt"].dt.strftime("%Y-%m-%d %H:%M:%S")

    out=[]

    for ticker,g in df.groupby("ticker"):
        g=g.sort_values("dt")
        g["sma_5"]=g["adj_close"].rolling(window=5,min_periods=1).mean()
        g["sma_20"]=g["adj_close"].rolling(window=20,min_periods=1).mean()
        g["daily_return"]=g["adj_close"].pct_change().fillna(0)
        out.append(g)
    
    result=pd.concat(out,ignore_index=True)
    
    result=result.rename(columns={"dt_iso":"dt"})
    return result[["ticker","dt","open","high","low","close","adj_close","volume","sma_5","sma_20","daily_return"]]