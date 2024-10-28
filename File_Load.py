import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from tqdm import tqdm
from colorama import Fore, Style, init
import psycopg2

init(autoreset=True)
load_dotenv()

username, password, dbname = os.getenv("USER"), os.getenv("PASSWORD"), os.getenv("DB_NAME")

# print(dbname)

def create_database_if_not_exists(username, password, dbname):
    conn_string = f"postgresql://{username}:{password}@localhost/postgres"
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{dbname}';")
    exists = cursor.fetchone()
    
    if not exists:
        cursor.execute(f'CREATE DATABASE {dbname};')
        print(f"{Fore.GREEN}Database '{dbname}' created successfully!{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Database '{dbname}' already exists!{Style.RESET_ALL}")
    
    cursor.close()
    conn.close()

create_database_if_not_exists(username, password, dbname)

conn_string = f'postgresql://{username}:{password}@localhost/{dbname}'
db = create_engine(conn_string)
conn = db.connect()

files = ['bonus', 'title', 'worker']

for file in tqdm(files, desc=f"{Fore.RED}Processing files...{Style.RESET_ALL}"):
    df = pd.read_csv(f'Data/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)

conn.close()
