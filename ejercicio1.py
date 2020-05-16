'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.'''
'''descuento = 0
lista_compra = {'naranjas':10, 'mandarinas':20, 'lechuga_manolo':30}

def descuento_(precio):
    descuento = input('Introduce el descuento del producto del producto:')
    precio_descontado = precio * (1-int(descuento)/100)
    return precio_descontado

def aplicar_iva (precio):
    precioconIVA = float(precio) * 1.21
    return precioconIVA

def calculo_cesta_compra(lista):
    total_compra = 0
    n = 1
    for values in lista:
        total_compra += aplicar_iva(descuento_(lista[values]))
    return total_compra

lista_compra = {'naranjas':10, 'mandarinas':20, 'lechuga_manolo':30}

print('El precio total es', str(calculo_cesta_compra(lista_compra))+'.')'''

'''def datos_personales():
    datos__={}
    nombre = input('¿Cuál es su nombre?: ')
    edad = input('¿Cuál es su edad?: ')
    direccion = input('¿Cuál es su dirección?: ')
    telefono = input('¿Cuál es tu telefono?: ')
    datos__['nombre'] = nombre
    datos__['edad'] = edad
    datos__['direccion'] = direccion
    datos__['telefono'] = telefono
    print(nombre, 'tiene', edad, ', vive en ', direccion, 'y su numero de telefono es', telefono+'.')
    return datos__

print(datos_personales())'''

'''Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, 
los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene 
restando la media y dividiendo por la desviación típica de la muestra.'''

'''def valores_atipico(lista):
    media = sum(lista)/len(lista)
    print(media)
    suma_diferencia = 0
    for item in lista:
        suma_diferencia += (item-media)**2
    from math import sqrt
    desviacion_tipica = sqrt(suma_diferencia/len(lista))
    print(desviacion_tipica)
    valores_lista_atipico = []
    for item in lista:
        atipico = (item-media)/desviacion_tipica
        if atipico < -3 or atipico >3:
            valores_lista_atipico.append(item)
    return valores_lista_atipico

print(valores_atipico([1,1,1,5000,200,200,200,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,3500]))'''

'''Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles 
cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo 
par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5'''

y = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def busqueda_filtro_precio(lista,presupuesto):
    busqueda_resultado = []
    for piso in lista:
        if piso['zona'] == 'A':
            precio1 = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + piso['garaje'] * 15000) * (1 - (2020-piso['año'])/100)   
            piso['precio'] = precio1
            if precio1.__int__ <= presupuesto:
                busqueda_resultado.append(piso)

        elif piso['zona'] == 'B':
            precio1 = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + piso['garaje'] * 15000) * (1 - (2020-piso['año'])/100) * 1,5
            piso['precio'] = precio1
            if precio1.__int__ <= presupuesto:
                busqueda_resultado.append(piso)
    return busqueda_filtro_precio

print(busqueda_filtro_precio(lista=y, presupuesto=254023))
