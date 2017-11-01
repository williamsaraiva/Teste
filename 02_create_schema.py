# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('customer.db')

# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)

"""
- Vamos criar uma tabela na base de dados chamada tb_customer_account.
id_customer – Identificação unica do cliente.
cpf_cnpj – CPF ou CNPJ do Cliente
nm_customer – Nome do Cliente
is_active – Indica se o cliente está ativo ou não
vl_total – Mostra quando que o cliente possui de saldo.
"""


cursor.execute("""
CREATE TABLE tb_customer_account (
        id_customer INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cpf_cnpj VARCHAR(14) NOT NULL,
        nm_customer NOT NULL,
        is_active BOOLEAN NOT NULL,
        vl_total money REAL
);
""")

print('Tabela criada com sucesso.')

# desconectando...
conn.close()