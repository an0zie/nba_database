from extract import extract_nba_stats
from transform import transform_nba_stats
from load import load_to_sqlite
from logger import setup_logger

logger = setup_logger()

def run_etl():
    logger.info("Starting extraction for season 2023-24...")
    raw_df = extract_nba_stats("2023-24")
    logger.info(f"Extracted {len(raw_df)} rows.")
    logger.info("Starting transformation...")
    clean_df = transform_nba_stats(raw_df)
    logger.info(f"After cleaning: {len(clean_df)} rows.")
    logger.info("Loading to database...")
    load_to_sqlite(clean_df)
    logger.info("ETL complete!")

if __name__ == "__main__":
    run_etl()