import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_nba_stats(season=2024):
    url =f"https://www.basketball-reference.com/leagues/NBA_{season}.html"

    headers = {"User ": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0  Safari/537.36 Edg/147.0.0.0"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")

    table = soup.find("table",{"id":"per_game_stats"})

    df =pd.read_html(str(table))[0]

    return df