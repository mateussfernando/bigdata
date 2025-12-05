import requests
import sqlite3

url = "http://universities.hipolabs.com/search?country=Brazil"

# Acessando o link da internet
response = requests.get(url)
response.raise_for_status()  
universities = response.json()


# Criar o banco e se concectar nele
con = sqlite3.connect("universidades.db")
c = con.cursor()

# Criar a tabela no banco
c.execute('''
CREATE TABLE IF NOT EXISTS universities
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
    c.execute('''INSERT INTO universities (name, country, state_province, web_pages, domains) VALUES (?,?,?,?,?);''',
              (university.get('name'), 
               university.get('country'), 
               university.get('state-province'), 
               ', '.join(university.get('web_pages', [])), 
               ', '.join(university.get('domains', []))))

con.commit()
con.close()