import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH= os.path.join(BASE_DIR, 'db', 'ecommerce.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'db', 'schema.sql')

DATA_SOURCE=os.path.join(BASE_DIR,"src","data","mock_data.json")