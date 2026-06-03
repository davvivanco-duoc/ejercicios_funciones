
productos = {}

def agregar_productos(productos):
    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede ser vacío")

    if nombre in productos:
        print("El producto existe")

    stock = int(input("Ingrese stock del producto: "))
    
    while True:
        precio = int(input("Ingrese precio del producto: "))
        try:
            if precio > 0 :
                break
        except ValueError:
            print("Debe ser numero, por favor vuelva a intentar")
            continue

    productos[nombre] = [stock, precio]

def mostrar_productos(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return
    for nombre in productos:
        print(f"{nombre} tiene {productos[nombre[0]]} a un precio de $ {productos[nombre[1]]} ")

def buscar_producto(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return
    nombre = input("NOmbre de producto a buscar").strip()

    if nombre in productos:
        print("Producto encontrado")
        print("Stock : ", productos[nombre[0]])
        print("Precio : ", productos[nombre[1]])

while True:
    print("-----MENU")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese una opcion"))
    except ValueError:
        print("Error, ingrese un número")
        continue


    if opcion == 1:
        print("agregar")
        agregar_productos(productos)
    elif opcion == 2:
        print("Mostrar")
    elif opcion == 3:
        print("Buscar")
    elif opcion == 4:
        print("agregar")
    if opcion == 5:
        break
    else:
        print("Opción no válida")
