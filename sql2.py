import sqlite3
import datetime

start = datetime.datetime.now()
db = sqlite3.connect("titanicDB.db")

# tabulu_nosaukumi = db.execute("""SELECT name FROM sqlite_schema 
# WHERE type = 'table';""")

# rezultats = tabulu_nosaukumi.fetchall()
# print(rezultats)

kolonnu_nosaukumi = db.execute("""SELECT name FROM pragma_table_info('titanic')
""")
rezultats = kolonnu_nosaukumi.fetchall()
#print(rezultats)
#1.variants
[print(rinda[0]) for rinda in rezultats]
#1.variants
# for rinda in rezultats:
#     print(rinda[0])

dati = db.execute("""SELECT Name,Age FROM titanic
ORDER BY Name
""")
rezultats = dati.fetchall()
#print(rezultats)
[print(rinda[0],',',rinda[1],end=':') for rinda in rezultats]

end = datetime.datetime.now()
laiks = end-start
print('\n')
print(laiks)
