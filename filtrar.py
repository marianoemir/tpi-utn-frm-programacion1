def filtrar_paises(lista_paises: list):
    """
    Permite filtrar los países según:
    1. Continente
    2. Rango de población
    3. Rango de superficie
    """

    if not lista_paises:
        print("No hay países cargados.")
        return

    while True:
        print("\n=== FILTRAR PAÍSES ===")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            continente = input("Ingrese el nombre del continente: ").strip().lower()
            resultados = [pais for pais in lista_paises if pais.continente.lower() == continente]
            if resultados:
                print(f"\nPaíses en el continente '{continente.capitalize()}':\n")
                for pais in resultados:
                    print(pais)
                print(f"\nTotal: {len(resultados)} país(es)")
            else:
                print(f"No se encontraron países en el continente '{continente}'.")

        elif opcion == "2":
            try:
                minimo = int(input("Ingrese el valor mínimo de población: "))
                maximo = int(input("Ingrese el valor máximo de población: "))
            except ValueError:
                print("Debe ingresar números válidos.")
                continue

            resultados = [pais for pais in lista_paises if minimo <= pais.poblacion <= maximo]
            if resultados:
                print(f"\nPaíses con población entre {minimo:,} y {maximo:,}:\n")
                for pais in resultados:
                    print(pais)
                print(f"\nTotal: {len(resultados)} país(es)")
            else:
                print("No se encontraron países en ese rango de población.")

        elif opcion == "3":
            try:
                minimo = int(input("Ingrese el valor mínimo de superficie: "))
                maximo = int(input("Ingrese el valor máximo de superficie: "))
            except ValueError:
                print("Debe ingresar números válidos.")
                continue

            resultados = [pais for pais in lista_paises if minimo <= pais.superficie <= maximo]
            if resultados:
                print(f"\nPaíses con superficie entre {minimo:,} y {maximo:,} km²:\n")
                for pais in resultados:
                    print(pais)
                print(f"\nTotal: {len(resultados)} país(es)")
            else:
                print("No se encontraron países en ese rango de superficie.")

        elif opcion == "0":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida, intente de nuevo.")
