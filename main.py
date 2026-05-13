from modulo_registro import registrar_ticket
from modulo_consulta import listar_tickets
from modulo_cierre import cerrar_ticket, reporte

while True:
    print("1. Registrar ticket")
    print("2. Ver tickets")
    print("3. Cerrar ticket")
    print("4. Reporte")
    print("5. Salir")
    # if/elif para cada opción...

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_ticket()

    elif opcion == "2":
        listar_tickets()

    elif opcion == "3":
        cerrar_ticket()

    elif opcion == "4":
        reporte()

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")