''' Python Fundamentos Ejercicios'''
'''def calcular_iva():
    n = 0
    while n < 1:
        precio = input('¿Cuál es el precio que quiere calcular?')
        try:
            precio = int(precio)
            n += 1
        except:
            print('Error al introducir la cantidad a calcular, por favor, introduce la cantidad de precio sin puntos ni comas, excepto para los decimales marcando con un punto')

    while n < 2:
        tipo_IVA = input('Introduce el tipo de IVA a calcular 21, 16 o 7:')      
        try:
            tipo_IVA = int(tipo_IVA)
            if tipo_IVA == 21 or tipo_IVA == 16 or tipo_IVA == 7:
                n +=1
            else:
                print('Error en el tipo de IVA, por favor introducie solo uno de los tres tipos impositivos')
        except:
            print('Error en el tipo de IVA, por favor solo introduce el numero sin %.')
       
    coste_del_iva = precio * (tipo_IVA/100)
    precio_total = precio + coste_del_iva
    return print('Precio inicial', precio, 'IVA aplicado', tipo_IVA,'Precio final', precio_total, 'Coste del IVA', coste_del_iva)        

calcular_iva()'''
