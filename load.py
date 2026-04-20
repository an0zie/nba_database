import sqlalchemy

def load_to_sqlite(df,db_path="nba_stats.db",table_name="player_stats"):
    engine=sqlalchemy.create_engine(f"sqlite:///{db_path}")

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} row into '{table_name}' table")