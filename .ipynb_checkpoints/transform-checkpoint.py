import pandas as pd

def transform_nba_stats(df):
    df= df[df["Player"] != "Player"]
    df =df.dropna(subset =["Player"])

    cols_to_convert = ["G","GS","MP","PTS","AST","TRB","STL","BLK","TOV"]
    for col in cols_to_convert:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.drop_duplicates(subset=["Player"] ,keep="first")
    df=df.reset_index(drop=True)
    df=df[["Player","Pos","Age","Tm","G","MP","PTS","AST","TRB","STL","BLK"]]

    return df