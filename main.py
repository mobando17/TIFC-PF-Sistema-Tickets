from modulo_registro import registrar_ticket
from modulo_consulta import listar_tickets
from modulo_cierre import cerrar_ticket, reporte

while True:
    print("1. Registrar ticket")
    print("2. Ver tickets")
    print("3. Cerrar ticket")
    print("4. Reporte")
    print("5. Salir")
    opcion = input("Selecciona: ")
    # if/elif para cada opción...
    if opcion == "2":
        listar_tickets()