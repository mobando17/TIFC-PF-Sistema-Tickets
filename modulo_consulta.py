# Función para listar los tickets
def listar_tickets(tickets):
    """
    Recorre la lista de tickets y los muestra en pantalla.
    Permite filtrar por estado: 'Abierto', 'Cerrado' o 'Todos'.
    """

    # Pedimos al usuario qué filtro quiere aplicar
    print("\n---BIENVENIDO AL MODULO DE CONSULTAS \n Consulta de Tickets ---")
    print("1. Mostrar solo Abiertos")
    print("2. Mostrar solo Cerrados")
    print("3. Mostrar Todos")
    opcion = input("Seleccione una opción (1-3): ")

    # Definimos el filtro según la opción elegida
    if opcion == "1":
        filtro = "Abierto"
    elif opcion == "2":
        filtro = "Cerrado"
    else:
        filtro = "Todos"

    # Si no hay tickets en la lista, mostramos mensaje
    if not tickets:
        print("\nNo hay tickets registrados.\n")
        return

    # Recorremos la lista de tickets
    print("\n--- Lista de Tickets ---")
    for ticket in tickets:
        # Si el filtro es 'Todos' mostramos todos
        # Si no, mostramos solo los que coincidan con el estado
        if filtro == "Todos" or ticket["estado"] == filtro:
            print(f"ID: {ticket['id']}")
            print(f"Descripción: {ticket['descripcion']}")
            print(f"Prioridad: {ticket['prioridad']}")
            print(f"Estado: {ticket['estado']}")
            print("-------------------------")
