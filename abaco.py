'''
Seudocodigo
imprimir instrucciones al usuario
usuario ingresa cifra
    separar cifra en unidad-decena-centena, etc {'1':5, '10': 2, '100':4, '1.000':4, '10.000':6, '100.000':6}
    aplicarle el formato
    Almacenamiento en lista['657.340', '1.051', '89']
    imprimir abaco
usuario ingresa nueva cifra
    repetir paso 3-4-5-6
si usuario ingresa salir
    imprimir lista de numeros
    byebye

'''

'''
Esqueleto de funciones
def input():
    #aqui va el break al leer salir
    return()

def separar_cifra():
    return()

def aplicar_formato():
    return()

def almacenar_en_lista():
    return()

def imprimir_abaco():
    return()

def 
'''






'''
# codigo salvador del profe, 70% de la prueba, wns pencas
def inicializar_tablero():
    tablero = []
    for i in range (0, 9):
        fila = []
        for j in range(0,6):
            fila.append(' ! ')
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero):
    tablero.reverse()
    for fila in tablero:
        for elemento in fila:
            print(elemento, sep = '', end= '')
        print()

def llenar_tablero(digitos, tablero):
    for j in range(0, 6):
        for i in range(0, digitos[j]):
            tablero[i][j] = ' X '
    return tablero

def preguntar_y_generar_digitos():
    numero = input('Ingrese un numero de 6 digitos: ')
    lista_numeros = list(numero)
    numeros_separados = []
    for elemento in lista_numeros:
        numeros_separados.append(int(elemento))
    return numeros_separados

tablero = inicializar_tablero()

print()
digitos = preguntar_y_generar_digitos()
tablero = llenar_tablero(digitos, tablero)
imprimir_tablero(tablero)
    


# Descompone un numero en unidades, decenas, centenas y unidades de millar.

print ("Introduce el número: ")
numero = int(input ())

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print("Unidades de millar: %i" % umil)
print ("Centenas: %i" % centenas)
print ("Decenas: %i" % decenas)
print ("Unidades: %i" % unidades)

'''