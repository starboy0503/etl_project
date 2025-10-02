from web3 import Web3
from config import WEB3_PROVIDER

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

if not w3.is_connected():
    raise Exception("❌ Could not connect to Ethereum node")

def get_latest_block_number():
    """Return latest block number"""
    return w3.eth.block_number

def get_block(block_number, full_transactions=False):
    """Fetch block data"""
    return w3.eth.get_block(block_number, full_transactions=full_transactions)
