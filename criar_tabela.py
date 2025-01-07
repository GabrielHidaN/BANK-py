import sqlite3

conn = sqlite3.connect('dataBase/data_base.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (cpf TEXT PRIMARY KEY, pass TEXT NOT NULL, nome TEXT NOT NULL , saldo INTERGER NOT NULL DEFAULT 1512)")

conn.commit()
conn.close()