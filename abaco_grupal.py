# Boris Aracena

#Parte 1: Definir formatos de los números ingresados, se leen como string, para trabajarlos en la posibilidad de errores y la palabra salir
def pregunta():
    numero = input('Ingrese un número de hasta 6 dígitos: ')
# Método lower convierte toda mayúscula a minúscula    
    while numero.lower != 'salir':
        if numero.lower() == 'salir':
           num_format = 'salir'
           diccionario = {}
           return num_format, diccionario
# Método isnumeric devuelve true o false al evaluar un string como número        
        elif numero.isnumeric() == False:
             numero = input('Ingresó letras, ingrese un número de hasta 6 dígitos: ')
        elif int(numero)>999999:
            numero = input('El número tiene más de 6 dígitos, intente nuevamente: ')
        else:
            break
        
    if numero.isnumeric() == True: 
        num_string = str(int(numero))
        n = len(num_string)
        if n <= 3:
            num_format = num_string
        else:
# Aquí se genera la magia de agregar el . al string de número            
            num_format = num_string[:n-3]+'.'+num_string[-3:]
        
        ceros = ''
        for i in range(6-n):
            ceros = ceros + '0'
# Función zip toma 2 objetos iterables y los convierte a una tupla que contiene un elemento de cada lista y los deja pareados, para trabajar en diccionario
        diccionario=dict(zip(['CM','DM','UM','C','D','U'],
                             list(ceros+num_string)))

    return num_format,diccionario


# Parte 2: Estructura de ábaco
def abaco_estructura(numero):
# Estructura de Strings 
    string1 = 'xxxxx'
    string2 = " | | "
    
    nn = int(numero)
# Contador hasta 10 porque la máxima altura que puede tomar es 9, por lectura maxima de número 999.999    
    count1 = nn
    if nn == 0:
        count2 = 10
    else:
        count2 = 10 - nn         
    
    lista1 = []
    lista2 = []
    
    for i in range(count1):
# Método append agrega un elemento al final de la lsita
        lista1.append(string1)
    
    for i in range(count2):
        lista2.append(string2)
     
    if nn==0:
        columna = [' +-+ ']+lista2+[' +-+ ']
    else:
        columna = [' +-+ ']+lista2+lista1+[' +-+ ']
        
    return columna


def llenar_tablero(diccionario):
    tablero=[]
    for x in diccionario:
        tablero.append(abaco_estructura(diccionario[x]))
        
    last_row = [' 100.000',' 10.000',' 1.000',' 100',' 10',' 1']
    
    for i in range(len(last_row)):
        tablero[i].append(last_row[i])
   
    return tablero
    
# El "rango 0:9 me permite asignar los espacios de la figura por columna y cambia hasta 5:7 para permitirme el equilibrio de impresión"
def imprimir_tablero(tablero):
    for tt in zip(tablero[0],tablero[1],tablero[2],
                  tablero[3],tablero[4],tablero[5]):

        print(f'{tt[0]:9} {tt[1]:8} {tt[2]:7} {tt[3]:7} {tt[4]:7} {tt[5]:7}')


# Probando
num_format = ''      
lista_intentos = []  
while num_format != 'salir':
    num_format,diccionario=pregunta()
    if num_format == 'salir' and len(lista_intentos) == 0:
        print('Usted salió del juego y no ingresó ningún número.\n¡Chao, pescao!')
        break
    elif num_format == 'salir' and len(lista_intentos) > 0:
        print('Usted salió del juego y sus intentos fueron:\n')
        for i in range(len(lista_intentos)):
# Dar el formato para presentación ordenada de los strings de números
            print(f'{lista_intentos[i]:>10}')
        print('\nGracias por participar, ¡adiós!')
        break
    else:
        lista_intentos.append(num_format)
        tablero = llenar_tablero(diccionario)
        imprimir_tablero(tablero)
    
    