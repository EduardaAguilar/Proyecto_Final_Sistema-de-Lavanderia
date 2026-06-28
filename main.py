# ==========================================================
# PROYECTO FINAL 
# Sistema de Gestión de Pedidos para una Lavandería
# ==========================================================

# ----------------------------------------------------------
# En esta lista se guardarán todos los pedidos que se registren.
# Cada pedido tendrá la información del cliente y del servicio.
# ----------------------------------------------------------
pedidos = []

# ----------------------------------------------------------
# Este número servirá para identificar cada pedido.
# Comienza en 1 y aumenta automáticamente.
# ----------------------------------------------------------
numero_pedido = 1

# ----------------------------------------------------------
# Aquí se guardan los tipos de servicio junto con su precio.
# Se utiliza un diccionario para que sea más fácil consultar
# la información cuando se registra un pedido.
# ----------------------------------------------------------
tarifas = {
    1: ("Ropa blanca", 5.00),
    2: ("Ropa de color", 6.00),
    3: ("Ropa delicada", 8.00),
    4: ("Cobijas y edredones", 12.00),
    5: ("Lavado exprés", 10.00)
}

# ----------------------------------------------------------
# Esta lista contiene los estados por los que puede pasar
# un pedido desde que ingresa hasta que se entrega.
# ----------------------------------------------------------
estados = [
    "Recibido",
    "En lavado",
    "Secando",
    "Listo para entrega",
    "Entregado"
]

# ----------------------------------------------------------
# FUNCIÓN: Mostrar menú principal
# Esta función muestra todas las opciones disponibles.
# El usuario elegirá una opción para utilizar el sistema.
# ----------------------------------------------------------

def mostrar_menu():

    print("\n===================================================")
    print("     SISTEMA DE GESTIÓN DE PEDIDOS")
    print("            LAVANDERÍA")
    print("===================================================")
    print("1. Registrar un pedido")
    print("2. Consultar un pedido")
    print("3. Mostrar todos los pedidos")
    print("4. Actualizar estado del pedido")
    print("5. Aplicar descuento")
    print("6. Eliminar un pedido")
    print("7. Mostrar resumen")
    print("8. Mostrar tarifas")
    print("9. Buscar pedidos por cliente")
    print("10. Salir del sistema")
    print("===================================================")

    # ----------------------------------------------------------
# FUNCIÓN: Mostrar tarifas
# Aquí se muestran los servicios disponibles junto con
# el valor que tiene cada uno.
# ----------------------------------------------------------

def mostrar_tarifas():

    print("\n============== TARIFAS ==============")

    print("1. Ropa blanca ............... $5.00")
    print("2. Ropa de color ............. $6.00")
    print("3. Ropa delicada ............. $8.00")
    print("4. Cobijas y edredones ....... $12.00")
    print("5. Lavado exprés ............. $10.00")

    print("=====================================")

    # ----------------------------------------------------------
# FUNCIÓN: Registrar un pedido
# En esta función se ingresan los datos del cliente,
# se selecciona el servicio y se guarda el pedido.
# ----------------------------------------------------------

def registrar_pedido():

    global numero_pedido

    print("\n========== REGISTRAR PEDIDO ==========")

    cliente = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el número de teléfono: ")

    # Se muestran las tarifas para que el usuario pueda elegir.
    mostrar_tarifas()

    servicio = int(input("Seleccione el tipo de servicio (1-5): "))

    # Si la opción no existe, el programa vuelve al menú.
    if servicio not in tarifas:
        print("La opción seleccionada no es válida.")
        return

    # Se pide la cantidad de prendas.
    cantidad = int(input("Ingrese la cantidad de prendas: "))

    # Si la cantidad es menor o igual a cero,
    # el pedido no puede registrarse.
    if cantidad <= 0:
        print("La cantidad de prendas debe ser mayor que cero.")
        return

    # Aquí se obtiene el nombre del servicio y su precio.
    nombre_servicio = tarifas[servicio][0]
    precio_servicio = tarifas[servicio][1]

    # Se calcula el valor total del servicio.
    costo = cantidad * precio_servicio

    # En este diccionario se guarda toda la información del pedido.
    pedido = {
        "numero": numero_pedido,
        "cliente": cliente,
        "telefono": telefono,
        "servicio": nombre_servicio,
        "cantidad": cantidad,
        "costo": costo,
        "descuento": 0,
        "estado": estados[0]
    }

    # El pedido se agrega a la lista general.
    pedidos.append(pedido)

    print("\nEl pedido fue registrado correctamente.")
    print("Número de pedido:", numero_pedido)
    print("Valor a pagar: $", format(costo, ".2f"))

    # Se aumenta el número para el siguiente pedido.
    numero_pedido += 1

    # ----------------------------------------------------------
# FUNCIÓN: Consultar un pedido
# Permite buscar un pedido utilizando su número.
# Si existe, se muestra toda la información registrada.
# ----------------------------------------------------------

def consultar_pedido():

    print("\n========== CONSULTAR PEDIDO ==========")

    # Primero se revisa si ya existen pedidos.
    if len(pedidos) == 0:
        print("Todavía no hay pedidos registrados.")
        return

    numero = int(input("Ingrese el número del pedido: "))

    # Se recorren todos los pedidos hasta encontrar el solicitado.
    for pedido in pedidos:

        if pedido["numero"] == numero:

            print("\nInformación del pedido")
            print("------------------------------")
            print("Número:", pedido["numero"])
            print("Cliente:", pedido["cliente"])
            print("Teléfono:", pedido["telefono"])
            print("Servicio:", pedido["servicio"])
            print("Cantidad de prendas:", pedido["cantidad"])
            print("Valor a pagar: $", format(pedido["costo"], ".2f"))
            print("Descuento:", pedido["descuento"], "%")
            print("Estado:", pedido["estado"])

            return

    print("No existe un pedido con ese número.")

    # ----------------------------------------------------------
# FUNCIÓN: Mostrar todos los pedidos
# Recorre la lista y presenta la información de cada pedido.
# ----------------------------------------------------------

def mostrar_pedidos():

    print("\n========== LISTA DE PEDIDOS ==========")

    # Si no hay pedidos registrados, se informa al usuario.
    if len(pedidos) == 0:
        print("Todavía no hay pedidos registrados.")
        return

    # Este ciclo muestra un pedido a la vez.
    for pedido in pedidos:

        print("--------------------------------------")
        print("Número:", pedido["numero"])
        print("Cliente:", pedido["cliente"])
        print("Servicio:", pedido["servicio"])
        print("Cantidad:", pedido["cantidad"])
        print("Valor: $", format(pedido["costo"], ".2f"))
        print("Estado:", pedido["estado"])

    print("--------------------------------------")

    # ----------------------------------------------------------
# FUNCIÓN: Actualizar estado del pedido
# Permite cambiar el estado de un pedido para llevar
# un control del proceso de lavado.
# ----------------------------------------------------------

def actualizar_estado():

    print("\n========== ACTUALIZAR ESTADO ==========")

    # Se revisa si ya existen pedidos registrados.
    if len(pedidos) == 0:
        print("Todavía no hay pedidos registrados.")
        return

    numero = int(input("Ingrese el número del pedido: "))

    # Se busca el pedido por su número.
    for pedido in pedidos:

        if pedido["numero"] == numero:

            print("\nSeleccione el nuevo estado:")
            print("1. Recibido")
            print("2. En lavado")
            print("3. Secando")
            print("4. Listo para entrega")
            print("5. Entregado")

            opcion = int(input("Opción: "))

            if opcion >= 1 and opcion <= 5:
                pedido["estado"] = estados[opcion - 1]
                print("El estado del pedido fue actualizado correctamente.")
            else:
                print("La opción ingresada no es válida.")

            return

    print("No existe un pedido con ese número.")

# ----------------------------------------------------------
# FUNCIÓN: Aplicar descuento
# Si un pedido tiene 10 prendas o más,
# se aplica un descuento del 10 %.
# ----------------------------------------------------------

def aplicar_descuento():

    print("\n========== APLICAR DESCUENTO ==========")

    if len(pedidos) == 0:
        print("Todavía no hay pedidos registrados.")
        return

    numero = int(input("Ingrese el número del pedido: "))

    for pedido in pedidos:

        if pedido["numero"] == numero:

            if pedido["cantidad"] >= 10:

                descuento = pedido["costo"] * 0.10

                pedido["descuento"] = 10
                pedido["costo"] = pedido["costo"] - descuento

                print("Se aplicó un descuento del 10 %.")
                print("Nuevo valor a pagar: $", format(pedido["costo"], ".2f"))

            else:

                print("Este pedido no cumple las condiciones para el descuento.")

            return

    print("No existe un pedido con ese número.")

    # ----------------------------------------------------------
# FUNCIÓN: Eliminar un pedido
# Permite borrar un pedido cuando sea necesario.
# ----------------------------------------------------------

def eliminar_pedido():

    print("\n========== ELIMINAR PEDIDO ==========")

    if len(pedidos) == 0:
        print("Todavía no hay pedidos registrados.")
        return

    numero = int(input("Ingrese el número del pedido: "))

    # Se busca el pedido para eliminarlo.
    for pedido in pedidos:

        if pedido["numero"] == numero:

            pedidos.remove(pedido)

            print("El pedido fue eliminado correctamente.")

            return

    print("No existe un pedido con ese número.")

    # ----------------------------------------------------------
# FUNCIÓN: Mostrar resumen
# Muestra cuántos pedidos hay registrados y el total
# de dinero acumulado por todos los servicios.
# ----------------------------------------------------------

def mostrar_resumen():

    print("\n========== RESUMEN ==========")

    if len(pedidos) == 0:
        print("Todavía no hay pedidos registrados.")
        return

    total = 0

    # Se suman los valores de todos los pedidos.
    for pedido in pedidos:
        total += pedido["costo"]

    print("Cantidad de pedidos:", len(pedidos))
    print("Total recaudado: $", format(total, ".2f"))


# ----------------------------------------------------------
# FUNCIÓN: Buscar pedidos por cliente
# Permite consultar todos los pedidos registrados
# con el nombre de un cliente.
# ----------------------------------------------------------

def buscar_cliente():

    print("\n========== BUSCAR CLIENTE ==========")

    if len(pedidos) == 0:
        print("Todavía no hay pedidos registrados.")
        return

    nombre = input("Ingrese el nombre del cliente: ")

    encontrado = False

    # Se revisan todos los pedidos registrados.
    for pedido in pedidos:

        if pedido["cliente"].lower() == nombre.lower():

            print("--------------------------------------")
            print("Número:", pedido["numero"])
            print("Servicio:", pedido["servicio"])
            print("Cantidad:", pedido["cantidad"])
            print("Valor: $", format(pedido["costo"], ".2f"))
            print("Estado:", pedido["estado"])

            encontrado = True

    if not encontrado:
        print("No se encontraron pedidos para ese cliente.")


# ----------------------------------------------------------
# PROGRAMA PRINCIPAL
# Desde aquí comienza la ejecución del sistema.
# El menú se repetirá hasta que el usuario elija salir.
# ----------------------------------------------------------

opcion = 0

while opcion != 10:

    mostrar_menu()

    try:

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_pedido()

        elif opcion == 2:
            consultar_pedido()

        elif opcion == 3:
            mostrar_pedidos()

        elif opcion == 4:
            actualizar_estado()

        elif opcion == 5:
            aplicar_descuento()

        elif opcion == 6:
            eliminar_pedido()

        elif opcion == 7:
            mostrar_resumen()

        elif opcion == 8:
            mostrar_tarifas()

        elif opcion == 9:
            buscar_cliente()

        elif opcion == 10:
            print("\nGracias por utilizar el sistema.")
            print("Fin del programa.")

        else:
            print("La opción ingresada no es válida.")

    except ValueError:
        print("Debe ingresar únicamente números.")





