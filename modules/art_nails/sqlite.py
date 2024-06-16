
import sqlite3

# funcion para insertar registros
def insert(id, username, name, t_number, edad, gender):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    #sql_str = 
    #cursor.execute('delete from clientes')
    sql_str = 'INSERT INTO clientes VALUES (' + str(id) + ", '" + username + "', '" + name + "', '" + t_number + "'," +  edad + ", '" + gender + "')"
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

def get_id(num):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('select telegramid from Clientes where tnumber = ' + str(num))
    rows = cursor.fetchall()
    connection.close()
    if rows:
        return rows[0][0]
    else:
        return False


#aa = get_id('Unbsvev3')

#print (aa)


def delete(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    #sql_str = 
    #cursor.execute('delete from clientes')
    sql_str = 'delete from Clientes where telegramid = ' + str(id)
    print (sql_str)
    cursor.execute(sql_str)
    connection.commit()
    connection.close()



	
