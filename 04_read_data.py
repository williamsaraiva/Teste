# 04_read_data.py
import sqlite3

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()
media = 0
count = 0
# lendo os dados
cursor.execute("""
SELECT nm_customer,vl_total FROM tb_customer_account
where id_customer between 1500 and 2700
and vl_total >= 560;
""")

for tupla in cursor.fetchall():
    media = tupla[1] + media
    count += 1

print("Média = R${0:.2f}".format(media/count))


cursor.execute("""
SELECT nm_customer,vl_total FROM tb_customer_account
where id_customer between 1500 and 2700
and vl_total >= 560
order by vl_total desc;
""")



for tupla in cursor.fetchall():
    print("Cliente: ",tupla[0], " Saldo: ", tupla[1])

conn.close()