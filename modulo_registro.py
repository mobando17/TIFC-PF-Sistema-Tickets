def registrar_ticket(tickets):
    """
    Registra un nuevo ticket en el sistema.
    """

    print("\n--- REGISTRO DE TICKETS ---")

    # Pedir descripción
    descripcion = input("Ingrese la descripción del problema: ").strip()

    # Validar descripción
    if descripcion == "":
        print("\n[ERROR] La descripción no puede estar vacía.")
        return

    # Pedir prioridad
    print("\nPrioridades disponibles:")
    print("1. Alta")
    print("2. Media")
    print("3. Baja")

    opcion = input("Seleccione prioridad (1-3): ")

    # Convertir opción a texto
    if opcion == "1":
        prioridad = "Alta"
    elif opcion == "2":
        prioridad = "Media"
    elif opcion == "3":
        prioridad = "Baja"
    else:
        print("\n[ERROR] Prioridad inválida.")
        return

    # Generar ID automático
    nuevo_id = f"T-{len(tickets)+1:03}"

    # Crear ticket
    ticket = {
        "id": nuevo_id,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Abierto"
    }

    # Guardar ticket
    tickets.append(ticket)

    print(f"\n[OK] Ticket registrado correctamente con ID: {nuevo_id}")