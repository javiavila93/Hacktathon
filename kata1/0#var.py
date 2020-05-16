def precio_del_pan():
    n=0
    while n < 1:
        pan_vendido = input('Introduce la cantidad de barras de pan vendidas: ')
        try:
            pan_vendido = int(pan_vendido)
            n += 1
        except:
            print('Error, introduce la cantidad con digitos, sin letras ni signos de puntuación.')
    precio = 3.49
    descuento = 1 - 0.6
    precio_pan_asentado = precio * descuento


    return print('Precio habitual', str(precio), '\nDescuento Aplicado', str(descuento), '\nCoste Final', str(precio_pan_asentado*pan_vendido))

precio_del_pan()