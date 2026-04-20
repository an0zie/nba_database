import pandas as pd

def transform_nba_stats(df):
    # Drop duplicates
    #df = df.drop_duplicates(subset=["PLAYER_NAME"], keep="first")
    df = df[~((df.duplicated(subset =["PLAYER_NAME"],keep=False)) &(df["TEAM_ABBREVIATION"] != "TOT"))]
    
    # Keep only useful columns
    df = df[["PLAYER_NAME", "TEAM_ABBREVIATION", "GP", "MIN", "PTS", "AST", "REB", "STL", "BLK"]]
    
    # Reset index
    df = df.reset_index(drop=True)
    
    return df