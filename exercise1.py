import funciones as fn

productos = {}

while True:
    print("-----MENU----------")
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
        fn.agregar_productos(productos)
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
