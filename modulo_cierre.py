def cerrar_ticket(ticket_id):
    # Ejercicio opcional
    # Busca el ID y cambia "Abierto" por "Cerrado"
    pass

def reporte():
    # Cuenta tickets por estado y prioridad
    # Muestra porcentajes
    
    print("Hola Mundo - Rama de Hermes")
    # modulo_cierre.py

def reporte(tickets):
    """
    Muestra estadísticas generales de los tickets registrados.
    """
    total = len(tickets)
    abiertos = 0 
    cerrados = 0
    # Diccionario para contar por prioridad 
    prioridades = {"Alta": 0, "Media": 0, "Baja": 0}

    for t in tickets:
        # Contar estados 
        if t["estado"] == "Abierto":
            abiertos += 1
        else:
            cerrados += 1
        
        # Contar prioridades 
        prio = t["prioridad"]
        if prio in prioridades:
            prioridades[prio] += 1

    print("\n" + "="*30)
    print("      REPORTE DE SOPORTE TI")
    print("="*30)
    print(f"Total de tickets: {total}")
    print(f"Tickets Abiertos: {abiertos}")
    print(f"Tickets Cerrados: {cerrados}")
    print("-" * 30)
    print(f"Prioridad Alta:  {prioridades['Alta']}")
    print(f"Prioridad Media: {prioridades['Media']}")
    print(f"Prioridad Baja:  {prioridades['Baja']}")
    print("="*30 + "\n")

def cerrar_ticket(tickets):
    """
    Busca un ticket por su ID y cambia su estado a 'Cerrado'.
    """
    # Pedir el ID al usuario 
    id_buscar = input("Ingrese el ID del ticket a cerrar (ej. T-001): ").strip().upper()
    encontrado = False

    for t in tickets:
        if t["id"] == id_buscar:
            t["estado"] = "Cerrado"
            print(f"\n[OK] El ticket {id_buscar} ha sido marcado como CERRADO.")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n[ERROR] No se encontró ningún ticket con el ID: {id_buscar}")
