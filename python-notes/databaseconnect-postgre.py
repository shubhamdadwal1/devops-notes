# import psycopg2
# conn=psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="Admin@123",
#     host="localhost",
#     port="5432"
# )
# conn.autocommit= True
# cur=conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS table5(id INT PRIMARY KEY, name VARCHAR(40), age INT)")
# #cur.execute("INSERT INTO table5(id, name, age) VALUES(%s, %s,%s)",(2,"shubhu",23))
# #cur.execute("CREATE TABLE IF NOT EXISTS table3( id INT PRIMARY KEY, name CHAR(50))")
# # cur.execute("INSERT INTO table3(id, name) VALUES (%s,%s)", (2,"shubh"))
# # cur.execute("INSERT INTO table3(id, name) VALUES (%s,%s)", (3,"arsh"))
# # cur.execute("INSERT INTO table3(id, name) VALUES (%s,%s)", (4,"sanju"))
# # cur.execute("INSERT INTO table3(id, name) VALUES (%s,%s)", (5,"sattu"))
# #cur.execute("UPDATE table3 SET name=%s WHERE id=%s",("shubham dadwal",1))
# #cur.execute("UPDATE table3 SET name=%s age=%s WHERE id=%s",("shubh dadwal",2,22))
# #cur.execute("UPDATE table5 SET name=%s, age=%s WHERE id=%s",("Shubham dadwal",22,1))
# cur.execute("DELETE FROM table5 WHERE id=%s ",(2,))
# cur.execute("SELECT * FROM table5")

# shu=cur.fetchall()
# print(shu)
# for row in shu:
#     print(row)
# cur.close()
# conn.close()