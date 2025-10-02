from datetime import datetime

def transform_block(block):
    """Convert raw block into dict"""
    return {
        "block_number": block.number,
        "block_hash": block.hash.hex(),
        "parent_hash": block.parentHash.hex(),
        "timestamp": datetime.utcfromtimestamp(block.timestamp),
        "tx_count": len(block.transactions),
        "gas_used": str(block.gasUsed),
        "gas_limit": str(block.gasLimit),
        "base_fee": str(getattr(block, "baseFeePerGas", 0))
    }

def transform_transactions(block):
    """Convert block.transactions into list of dicts"""
    rows = []
    for tx in block.transactions:
        rows.append({
            "tx_hash": tx.hash.hex(),
            "block_number": block.number,
            "from_address": tx["from"],
            "to_address": tx["to"],
            "value": str(tx["value"]),
            "gas": str(tx["gas"]),
            "gas_price": str(tx["gasPrice"]),
            "nonce": str(tx["nonce"]),
            "tx_index": tx["transactionIndex"]
        })
    return rows
