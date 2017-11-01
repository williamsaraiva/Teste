# customer_db.py
# 01_create_db.py
import sqlite3

print("Criando base de dados...")
conn = sqlite3.connect('customer.db')

conn.close()
print("Base de dados criada com sucesso...")