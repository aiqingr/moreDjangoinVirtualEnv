import sqlite3


conn = sqlite3.connect('myqutoes.db')
curr = conn.cursor()

# curr.execute("""create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text
#                 )""")

curr.execute("""insert into quotes_tb values ('python scrapy', 'Nick', 'Scrapy')""")

conn.commit()
conn.close()
