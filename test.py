import sqlite as sql

sql.insert (6573427258, 'fuan', '856995588', '2025-05-14')

a = sql.exists(1256)
if a:
    print (a[0][0])
else:
    print ('no one')