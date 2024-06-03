
import sqlite3

# funcion para insertar registros
def insert(id, username, name, edad, gender):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    #sql_str = 
    #cursor.execute('delete from clientes')
    sql_str = 'INSERT INTO clientes VALUES (' + str(id) + ", '" + username + "', '" + name + "', " +  str(edad) + ", '" + gender + "')"
    cursor.execute(sql_str)
    connection.commit()
    connection.close()

# funcion para ver si el cliente existe ya
def exists(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('select name from Clientes where TelegramID = ' + str(id))
    rows = cursor.fetchall()
    connection.close()
    if rows:
        return rows[0][0]
    else:
        return False


def delete(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    #sql_str = 
    #cursor.execute('delete from clientes')
    sql_str = 'delete from clientes where telegramid = ' + str(id)
    print (sql_str)
    cursor.execute(sql_str)
    connection.commit()
    connection.close()




'''
insert (125656544412, 'jewrfuan', '856995588', '2025-05-14')
a = exists(125656544412)
if a:
    print (a[0][0])
else:
    print ('no one')
'''