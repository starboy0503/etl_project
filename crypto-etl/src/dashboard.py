import sys, os
# Add parent folder (project root) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

from config import DB_PATH

engine = create_engine(f"sqlite:///{DB_PATH}")

# Get latest 200 rows for plotting
df = pd.read_sql("SELECT * FROM crypto_prices ORDER BY timestamp DESC LIMIT 200", engine)

fig = px.line(df, x="timestamp", y="price", color="coin",
              title="Crypto Prices Over Time", markers=True)
fig.show()
