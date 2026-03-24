equipos = {}

while True:
    print("\n1. Agregar equipo")
    print("2. Registrar resultado")
    print("3. Mostrar tabla")
    print("4. Eliminar equipo")
    print("5. Salir")

    opcion = input("Opcion: ")


    # AGREGAR EQUIPO
    if opcion == "1":
        nombre = input("Nombre del equipo: ")

        if nombre in equipos:
            print("El equipo ya existe")
        else:
            equipos[nombre] = 0
            print("Equipo agregado")

    # REGISTRAR RESULTADO
    elif opcion == "2":
        local = input("Equipo local: ")
        visitante = input("Equipo visitante: ")

        if local not in equipos or visitante not in equipos:
            print("Equipo no existe")
            continue

        marcador = input("Marcador (ej: 2 1): ")
        partes = marcador.split()

        if len(partes) != 2:
            print("Formato invalido")
            continue

        if not partes[0].isdigit() or not partes[1].isdigit():
            print("Formato invalido")
            continue

        goles_local = int(partes[0])
        goles_visitante = int(partes[1])

        if goles_local > goles_visitante:
            equipos[local] += 3
        elif goles_local < goles_visitante:
            equipos[visitante] += 3
        else:
            equipos[local] += 1
            equipos[visitante] += 1

        print("Resultado cargado")

    # MOSTRAR TABLA 
    elif opcion == "3":
        print("\nTabla de posiciones:")

        # convertir a lista
        lista = list(equipos.items())

        # ordenar
        for i in range(len(lista)):
            for j in range(len(lista) - 1):
                if lista[j][1] < lista[j + 1][1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux

        # mostrar
        for equipo, puntos in lista:
            print(equipo, "-", puntos)

    # ELIMINAR
    elif opcion == "4":
        nombre = input("Equipo a eliminar: ")

        if nombre in equipos:
            del equipos[nombre]
            print("Eliminado")
        else:
            print("No existe")

    # SALIR
    elif opcion == "5":
        print("Fin del programa")
        break
    else:
        print("Opcion invalida")