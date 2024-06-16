
#verificar la edad
def edad(age):
    try:
        age = int(age)
        if not age:
            rtn = 'Tiene que ser un numero, prueba otra vex'
        elif age < 18:
            rtn = 'Eres muy joven, prueba otra vex'
        elif age > 110:
            rtn = 'tienes demasiada edad, prueba otra vex'
        else:
            rtn = 'ok'
    except:
        rtn ='Tiene que ser entre 18 y 110, si estas fuera de ese rango'
    return rtn



def t_number(num):
    try:
        if not isinstance(int(num), int):
            rtn = 'Tiene que ser un numero'
        elif len(num) != 9:
            rtn = 'the telephone number should be 9 digits'
        else:
            rtn = 'ok'
    except:
        rtn ='Tiene que ser un numero de 9 digitos'

    return rtn



