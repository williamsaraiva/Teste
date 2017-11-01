# 03_create_data.py
import random
import sqlite3

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()

# criando uma lista de dados
nomes = ['Marco','Fausto','Bruno','Adriano','Felipe','Franco','Gil']
sobrenomes=['Alves','Fanti','Sutter','Pereira','Torres']


lista = []

for x in range(5000):
    lista.append((random.randrange(10000000000,99999999999), random.choice(nomes) + ' ' + random.choice(sobrenomes),
     random.randrange(0,2),round(random.uniform(0,1000),2)))


# inserindo dados na tabela
cursor.executemany("""
            INSERT INTO tb_customer_account (cpf_cnpj, nm_customer, is_active, vl_total)
            VALUES (?,?,?,?)
            """, lista)

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()