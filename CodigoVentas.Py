productos=[]
sumSinIva=0
total=0
totalIva=0

while (True):
    COD = input('Número de Código: ')
    nombre=input('Artículo: ')
    precio = float (input ('Precio del artículo con iva: '))
    iva = float (input('iva: '))
    cantidad = int (input('Cantidad: '))
    valorSinIva = precio/(1+(iva/100))
    sumSinIva=sumSinIva+(valorSinIva*cantidad)
    total=total+(precio*cantidad)
    totalIva=totalIva+(valorSinIva*iva*cantidad/100)

    dato = {'Codigo': COD, 'Nombre':nombre, 'Precio': precio, 'Iva': iva,'Cantidad': cantidad, 'SinIva':valorSinIva}
    productos.append(dato)

    x = input('¿Algún otro artículo? y/n: ')
    if x == 'n': break
print ('Código\t','Artículo\t','Precio con Iva\t','Cantidad\t','Valor sin IVa')
for i in productos:
    print(i['Codigo'],'\t',i['Nombre'],'\t','$',i['Precio'],'\t',i['Iva'],'%','\t',i['Cantidad'],'\t','$',i['SinIva'])

print('///////////////')
print('Subtotal: ','\t','$',sumSinIva)
print('Iva:    ','\t','$',totalIva)
print('Total: ','\t','$',total)
print('///////////////')
