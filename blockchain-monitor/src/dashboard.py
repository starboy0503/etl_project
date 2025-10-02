import streamlit as st
import pandas as pd
import sqlite3
from config import DB_PATH


# Utility to load data safely
def load_data(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df


# ---------------- DASHBOARD ----------------
st.set_page_config(page_title="Ethereum Monitor", layout="wide")
st.title("⛓ Simple Ethereum Blockchain Dashboard")

# --- BLOCKS ---
st.header("📦 Latest Blocks")
try:
    blocks = load_data("""
        SELECT block_number, timestamp, tx_count, gas_used, gas_limit, base_fee
        FROM blocks
        ORDER BY block_number DESC
        LIMIT 10
    """)
    if blocks.empty:
        st.warning("⚠️ No block data found.")
    else:
        st.dataframe(blocks)

        # --- Graphs for Blocks ---
        st.subheader("📊 Transactions per Block")
        st.bar_chart(blocks.set_index("block_number")["tx_count"])

        st.subheader("⛽ Gas Used vs Gas Limit")
        st.line_chart(blocks.set_index("block_number")[["gas_used", "gas_limit"]])
except Exception as e:
    st.error(f"❌ Error reading blocks: {e}")


# --- TRANSACTIONS ---
st.header("💸 Recent Transactions")
try:
    txs = load_data("""
        SELECT tx_hash, block_number, from_address, to_address, value
        FROM transactions
        ORDER BY block_number DESC
        LIMIT 10
    """)
    if txs.empty:
        st.warning("⚠️ No transactions found.")
    else:
        st.dataframe(txs)

        # --- Graph for Transactions Value ---
        st.subheader("💵 Transaction Values (Last 10)")
        st.bar_chart(txs.set_index("tx_hash")["value"])
except Exception as e:
    st.error(f"❌ Error reading transactions: {e}")
