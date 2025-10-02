import time
import logging
from extract import get_latest_block_number, get_block
from transform import transform_block, transform_transactions
from load import load_block, load_transactions
from config import POLL_INTERVAL_SECONDS

logging.basicConfig(level=logging.INFO)
last_seen = None

def run_realtime():
    """Run ETL in continuous realtime mode"""
    global last_seen
    while True:
        try:
            latest = get_latest_block_number()
            if last_seen is None:
                start = max(0, latest - 5)  # look back a few blocks
            else:
                start = last_seen + 1

            for bn in range(start, latest + 1):
                block = get_block(bn, full_transactions=True)
                block_data = transform_block(block)
                txs = transform_transactions(block)
                load_block(block_data)
                load_transactions(txs)
                logging.info(f"✅ Ingested block {bn} with {len(txs)} txs")
                last_seen = bn

        except Exception as e:
            logging.exception("❌ ETL error: %s", e)

        time.sleep(POLL_INTERVAL_SECONDS)

def run_batch(n_blocks=10):
    """Fetch last N blocks once"""
    latest = get_latest_block_number()
    start = latest - n_blocks + 1
    for bn in range(start, latest + 1):
        block = get_block(bn, full_transactions=True)
        block_data = transform_block(block)
        txs = transform_transactions(block)
        load_block(block_data)
        load_transactions(txs)
        logging.info(f"✅ Ingested block {bn} with {len(txs)} txs")

if __name__ == "__main__":
    # Choose mode:
    # run_realtime()
    run_batch(20)
