from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

mysql_host = os.getenv('HOST')
mysql_user = os.getenv('USER')
mysql_password = os.getenv('KEY')
mysql_data = os.getenv('DATABASE')

db = create_engine(f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_data}')

query = 'select * from db1.UEFA;'
query 

df = pd.read_sql(query, con = db)
df

df2 = pd.read_csv('data/HospInfo.csv')
df2.to_sql('some_table', con = db, if_exists = 'replace')