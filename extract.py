from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

def extract_nba_stats(season="2023-24"):
    print("Fetching NBA stats from official API...")
    
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season
    )
    
    df = stats.get_data_frames()[0]
    return df