
import sqlite3

# funcion para insertar registros
def insert(id, name, edad, gender, when):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    #sql_str = 
    #cursor.execute('delete from clientes')
    cursor.execute('INSERT INTO clientes (TelegramID, Name, Edad, Genero, Inscrito) VALUES (?, ?, ?, ?, ?)', (id, name, edad, gender, when))
    connection.commit()
    connection.close()

# funcion para ver si el cliente existe ya
def exists(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM clientes where TelegramID = ' + str(id))
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
    sql_str = 'delete from clientes where TelegramID = ' + str(id)
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