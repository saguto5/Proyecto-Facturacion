# Tienda
class Producto:
    def __init__(self,codigoProducto, nombreProducto, precio, cantidad, iva, total, totalSinImpuestos, impuesto):
        self.codigoProducto = codigoProducto
        self.nombreProducto = nombreProducto
        self.precio = precio
        self.cantidad = cantidad
        self.iva = iva
        self.total = total
        self.totalSinImpuestos = totalSinImpuestos
        self.impuesto = impuesto


class Tienda:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.listaDeProductos = []
    
    def agregarProductos(self,productoAAgregar):
        self.listaDeProductos.append(productoAAgregar)
    
    def imprimirLista(self):
        for producto in self.listaDeProductos:
            print("___________")
            print("Codigo Producto: ", producto.codigoProducto)
            print("Producto: ", producto.nombreProducto)
            print("Precio: ", producto.precio)
            print("Cantidad: ", producto.cantidad)
            print("IVA: ", producto.iva)
            print("___________")

    def imprimirFactura(self):
        
        for producto in self.listaDeProductos:
            print("___________")
            print("Codigo Producto: ", producto.nombreProducto)
            print("Valor TOTAL: ", producto.total)
            print("Valor total sin IVA: ", producto.totalSinImpuestos)
            print("Valor IVA: ", producto.impuesto)

        print("___________")

  
nombre = input("Ingrese su nombre: ")
tienda = Tienda(nombre)


while True:
    operacion = input("Ingrese A para ingresar un producto, I para imprimir los productos e inventarios, F para facturacion: ")
    if operacion == "A":
        
        codigoProducto = input("Ingrese el numero de producto: ")
        nombreProducto = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        iva = int(input("Digite el porcentaje de iva: "))
        total = cantidad * precio
        totalSinImpuestos = (total*100)/(100+iva)
        impuesto = total - totalSinImpuestos
      


        productoCreado = Producto(codigoProducto, nombreProducto, precio, cantidad, iva, total, totalSinImpuestos, impuesto)
        tienda.agregarProductos(productoCreado)
    
    elif operacion == "I":
        tienda.imprimirLista()
    
    elif operacion == "F":
        tienda.imprimirFactura()
        
