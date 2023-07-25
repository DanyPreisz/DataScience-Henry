# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def NumeroCapicua(numero):
    '''
    En matemáticas, la palabra capicúa (del catalán cap i cua, 'cabeza y cola')
    se refiere a cualquier número que se lee igual de izquierda a derecha que 
    de derecha a izquierda. Se denominan también números palíndromos.
    Esta función devuelve el valor booleano True si el número es capicúa, de lo contrario
    devuelve el valor booleano False 
    En caso de que el parámetro no sea de tipo entero, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se evaluará si es capicúa o no lo es.
    Ej:
        NumeroCapicua(787) debe retornar True
        NumeroCapicua(108) debe retornar False
    '''
    #Tu código aca:
    if not isinstance(numero, int):
        return None

    numero_str = str(numero)
    return numero_str == numero_str[::-1]


def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if type(numero) != int:
        return None
    if numero < 1: 
        return None
    factorial = 1
    while (numero > 1):
        factorial = factorial * numero      #(factorial*=numero)
        numero = numero - 1                 #(numero-=1)
    return factorial

def ProximoPrimo(actual_primo):
    '''
    Esta función devuelve el número primo siguiente al enviado como parámetro.
    En caso de que el parámetro no sea de tipo entero y/o no sea un número primo, debe retornar nulo.
    Recibe un argumento:
        actual_primo: Será el número primo a partir del cual debo buscar el siguiente
    Ej:
        ProximoPrimo(7) debe retornar 11
        ProximoPrimo(8) debe retornar nulo
    '''
    #Tu código aca:
    if not isinstance(actual_primo, int) or actual_primo < 2:
        return None

    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    siguiente_primo = actual_primo + 1
    while not es_primo(siguiente_primo):
        siguiente_primo += 1

    return siguiente_primo

def FactorizarNumero(numero):
    '''
    Esta función recibe como parámetro un número entero mayor a cero y devuelva dos listas, 
    una con cada factor común y otra con su exponente, 
    esas dos listas tienen que estar contenidas en otra lista.
    En caso de que el parámetro no sea de tipo entero y/ó mayor a cero debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se hará la factorización.
    Ej:

        factorizar_numero(12) debe retornar [[2,3],[2,1]]
        factorizar_numero(13) debe retornar [[13],[1]]
        factorizar_numero(14) debe retornar [[2,7],[1,1]]
    '''
    #Tu código aca:
    def FactorizarNumero(numero):
        if not isinstance(numero, int) or numero <= 0:
            return None

    factores = []
    exponentes = []

    divisor = 2

    while divisor <= numero:
        exponente = 0

        while numero % divisor == 0:
            numero //= divisor
            exponente += 1

        if exponente > 0:
            factores.append(divisor)
            exponentes.append(exponente)
        divisor += 1

    return [factores, exponentes]


def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    #Tu código aca:
    if not (type(lista) is list):
        return None
    lista1 = lista.copy()
    resultado = []
    while len(lista1) > 0:
        current = lista1.pop(0)
        if isinstance(current, int) or isinstance(current, str):
            resultado.append(current)

        if isinstance(current, list):
            for i in range(len(current) - 1, -1, -1):
                lista1.insert(0, current[i])

        if len(lista1) == 0:
            return resultado


def ClaseVehiculo(tipo, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Vehiculo, 
    la cual debe tener los siguientes atributos:
        Tipo:       Un valor dentro de los valores posibles: ['auto','camioneta','moto']
        Color:      Un valor de tipo de dato string.
        Velocidad:  Un valor de tipo de dato float, que debe inicializarse en cero.
    y debe tener el siguiente método:
        Acelerar(): Este método recibe un parámetro con el valor que debe incrementar a la
                    propiedad Velocidad y luego retornarla.
                    Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
                    Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
    Recibe dos argumento:
        tipo: Dato que se asignará al atributo Tipo del objeto de la clase Vehiculo
        color: Dato que se asignará al atributo Color del objeto de la clase Vehiculo
    Ej:
        a = ClaseVehículo('auto','gris')
        a.Acelerar(10) -> debe devolver 10
        a.Acelerar(15) -> debe devolver 25
        a.Acelerar(-10) -> debe devolver 15
    '''
    #Tu código aca:
    class Vehiculo:
        def __init__(self, tipo: str, color: str):
            self.Tipo = tipo
            self.Color = color
            self.Velocidad = float(0)

        def Acelerar(self, delta):
            nuevo = self.Velocidad + delta
            if nuevo < 0:
                self.Velocidad = 0
            elif nuevo > 100:
                self.Velocidad = 100
            else:
                self.Velocidad = nuevo
            return self.Velocidad

    nuevoVehiculo = Vehiculo(tipo, color)

    return nuevoVehiculo


def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
    if not isinstance(diccionario_par, dict) or clave not in diccionario_par:
        return None

    indices_ordenados = sorted(range(len(diccionario_par[clave])), key=lambda i: diccionario_par[clave][i], reverse=descendente)

    diccionario_ordenado = {}
    for key in diccionario_par:
        diccionario_ordenado[key] = [diccionario_par[key][i] for i in indices_ordenados]

    return diccionario_ordenado