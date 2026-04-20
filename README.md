# 🏀 NBA Player Stats ETL Pipeline

A data engineering project that extracts live NBA player statistics from the official NBA API, transforms and cleans the data using Python and pandas, and loads it into a SQLite database for analysis.

---

## 📋 Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline built from scratch using Python. It pulls per-game statistics for all NBA players in a given season, cleans the data, and stores it in a structured database that can be queried with SQL.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.13 | Core programming language |
| nba_api | Fetches official NBA player statistics |
| pandas | Data cleaning and transformation |
| SQLAlchemy | Database connection and loading |
| SQLite | Local database storage |
| logging | Pipeline monitoring and error tracking |

---

## 📁 Project Structure

```
nba_etl/
├── extract.py       # Pulls player stats from the NBA API
├── transform.py     # Cleans and structures the raw data
├── load.py          # Saves clean data to SQLite database
├── logger.py        # Sets up logging to terminal and log file
├── main.py          # Orchestrates the full ETL pipeline
├── nba_stats.db     # Generated SQLite database (auto-created on run)
├── etl.log          # Generated log file (auto-created on run)
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

### Extract
Connects to the official NBA API using the `nba_api` Python package and pulls per-game player statistics for any season you choose. When you run the pipeline, it will prompt you to type the season you want directly in the terminal. No web scraping involved — data comes directly from the NBA's own data system.

### Transform
Cleans the raw data by:
- Removing duplicate player entries caused by mid-season trades
- Keeping the combined season totals (`TOT`) for traded players instead of team-specific splits
- Selecting only the most relevant statistical columns
- Resetting the DataFrame index for clean database storage

### Load
Saves the cleaned DataFrame into a local SQLite database (`nba_stats.db`) using SQLAlchemy. The table is replaced on every run to ensure the data stays fresh.

### Logging
Every step of the pipeline is logged with timestamps to both the terminal and a persistent `etl.log` file, making it easy to monitor runs and debug issues.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.x installed on your machine.

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/nba-etl.git
cd nba-etl
```

**2. Install required packages**
```bash
pip install nba_api pandas sqlalchemy lxml
```

**3. Run the pipeline**
```bash
python main.py
```

---

## 📊 Output

After running the pipeline you will be prompted to choose a season, then see output like this:

```
Available seasons: 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24
Enter the season you want (e.g. 2023-24): 2022-23

Fetching NBA stats for 2022-23...
2026-04-20 03:53:42 [INFO] Extracted 572 rows for season 2022-23.
2026-04-20 03:53:43 [INFO] Starting transformation...
2026-04-20 03:53:43 [INFO] After cleaning: 560 rows.
2026-04-20 03:53:43 [INFO] Loading to database...
2026-04-20 03:53:44 [INFO] ETL complete for season 2022-23!
```

Two files will be generated in your project folder:
- **`nba_stats.db`** — SQLite database containing the player stats table
- **`etl.log`** — Log file recording every step of the pipeline run

---

## 🗄️ Database Schema

The `player_stats` table contains the following columns:

| Column | Type | Description |
|---|---|---|
| PLAYER_NAME | TEXT | Full name of the player |
| TEAM_ABBREVIATION | TEXT | Team the player played for |
| GP | INTEGER | Games played |
| MIN | FLOAT | Average minutes per game |
| PTS | INTEGER | Average points per game |
| AST | INTEGER | Average assists per game |
| REB | INTEGER | Average rebounds per game |
| STL | INTEGER | Average steals per game |
| BLK | INTEGER | Average blocks per game |

---

## 🔍 Viewing the Data

You can explore the database visually using **DB Browser for SQLite** (free download at [sqlitebrowser.org](https://sqlitebrowser.org)).

Or query it directly using SQL in Python:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("nba_stats.db")
df = pd.read_sql("SELECT * FROM player_stats ORDER BY PTS DESC LIMIT 10", conn)
print(df)
```

---

## 🎮 Interactive Season Selection

When you run the pipeline it will automatically ask you which season you want:

```
Available seasons: 2015-16, 2016-17, 2017-18, 2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24
Enter the season you want (e.g. 2023-24):
```

Just type the season in the format shown and press Enter. The pipeline will fetch, clean and load that season's data automatically. You can run it multiple times with different seasons to compare data across years.

---

## 📌 Key Concepts Demonstrated

- **ETL pipeline architecture** — separation of extract, transform, and load into distinct modules
- **API data ingestion** — connecting to and consuming a real-world sports data API
- **Interactive user input** — terminal prompts that let the user choose which season to load
- **Data cleaning** — handling duplicates, selecting columns, and resetting indexes
- **Database loading** — writing structured data to a relational database using SQLAlchemy
- **Pipeline logging** — professional monitoring of each stage with timestamps

---

## 👤 Author

**Anozie**
Computer Science Student | Aspiring Data Engineer
Budapest, Hungary

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
