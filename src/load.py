import sqlite3
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class Load():

    def __ini__(self):
        pass

    def load_data_sqlite(self, universities, table_name):
        # Criar o banco e se concectar nele
        con = sqlite3.connect("universidades.db")
        c = con.cursor()

        # Criar a tabela no banco
        c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name}
                (
                id INTERGER PRIMARY KEY,
                name TEXT,
                country TEXT,
                state_province TEXT,
                web_pages TEXT,
                domains TEXT
                );
        ''')

        for university in universities: 
            c.execute(f'''INSERT INTO {table_name} (name, country, state_province, web_pages, domains) VALUES (?,?,?,?,?);''',
                    (university.get('name'), 
                    university.get('country'), 
                    university.get('state-province'), 
                    ', '.join(university.get('web_pages', [])), 
                    ', '.join(university.get('domains', []))))

        con.commit()
        con.close()

    def load_data_atlas(self, universities, db_name=None, collection_name=None):
        uri = os.getenv("MONGO_URI")

        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]

        if universities:
            collection.insert_many(universities)

        client.close()