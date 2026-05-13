from modulo_registro import registrar_ticket
from modulo_consulta import listar_tickets
from modulo_cierre import cerrar_ticket, reporte


tickets = []

while True:

    print("\n========== SISTEMA DE TICKETS ==========")
    print("1. Registrar ticket")
    print("2. Ver tickets")
    print("3. Cerrar ticket")
    print("4. Reporte")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    
    if opcion == "1":
        registrar_ticket(tickets)
    
    elif opcion == "2":
        listar_tickets(tickets)

    
    elif opcion == "3":
        cerrar_ticket(tickets)

    
    elif opcion == "4":
        reporte(tickets)

    
    elif opcion == "5":
        print("\nSaliendo del sistema...")
        break

    
    else:
        print("\n[ERROR] Opción inválida. Intente nuevamente.")
   
