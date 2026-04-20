from extract import extract_nba_stats
from transform import transform_nba_stats
from load import load_to_sqlite
from logger import setup_logger

logger = setup_logger()

def run_etl(season=2024):
    logger.info(f"Starting extraction for season{season} ....")
    raw_df=extract_nba_stats(season)
    logger.info(f"Extracted {len(raw_df)} rows.")

    logger.info("Strating transformation ....")
    clean_df =transform_nba_stats(raw_df)
    logger.info(f"After cleaning : {len(clean_df)} rows.")

    logger.info("Loading to database ....")
    load_to_sqlite(clean_df)
    logger.info("ETL complete !")

    if _name_ == "_main_":
        run_etl()