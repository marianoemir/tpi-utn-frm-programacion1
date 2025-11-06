import os
from Paisdelmundo import Paisdelmundo


# Detectar automáticamente la ruta del archivo CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(BASE_DIR, "paises.csv")


# === Filtrar países por distintos criterios ===
def filtrar_paises(lista_paises: list):
    if not lista_paises:
        print("No hay países cargados.")
        return

    while True:
        print("\n=== FILTRAR PAÍSES ===")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("0. Volver")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            continente = input(
                "Ingrese el nombre del continente: ").strip().lower()
            resultados = [p for p in lista_paises if Paisdelmundo.quitar_acentos(p.continente.lower()) ==
                          Paisdelmundo.quitar_acentos(continente)]
            if resultados:
                print(f"\nPaíses en '{continente.capitalize()}':\n")
                for pais in resultados:
                    print(pais)
                print(f"\nTotal: {len(resultados)} país(es)")
            else:
                print("No se encontraron países en ese continente.")

        elif opcion == "2":
            try:
                minimo = int(input("Población mínima: "))
                maximo = int(input("Población máxima: "))
            except ValueError:
                print("Ingrese valores numéricos válidos.")
                continue
            resultados = [p for p in lista_paises if minimo <=
                          p.poblacion <= maximo]
            for pais in resultados:
                print(pais)
            print(f"\nTotal: {len(resultados)} país(es)")

        elif opcion == "3":
            try:
                minimo = int(input("Superficie mínima: "))
                maximo = int(input("Superficie máxima: "))
            except ValueError:
                print("Ingrese valores numéricos válidos.")
                continue
            resultados = [p for p in lista_paises if minimo <=
                          p.superficie <= maximo]
            for pais in resultados:
                print(pais)
            print(f"\nTotal: {len(resultados)} país(es)")

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

# === Funciones de ordenamiento ===


def ordenar_paises_por_nombre(lista_paises: list):
    for i in range(len(lista_paises)):
        for j in range(i+1, len(lista_paises)):
            if lista_paises[i].nombre > lista_paises[j].nombre:
                aux = lista_paises[i]
                lista_paises[i] = lista_paises[j]
                lista_paises[j] = aux
    return lista_paises


def ordenar_paises_por_poblacion(lista_paises: list):
    for i in range(len(lista_paises)):
        for j in range(i+1, len(lista_paises)):
            if lista_paises[i].poblacion > lista_paises[j].poblacion:
                aux = lista_paises[i]
                lista_paises[i] = lista_paises[j]
                lista_paises[j] = aux
    return lista_paises


def ordenar_paises_por_superficie(lista_paises: list):
    for i in range(len(lista_paises)):
        for j in range(i+1, len(lista_paises)):
            if lista_paises[i].superficie > lista_paises[j].superficie:
                aux = lista_paises[i]
                lista_paises[i] = lista_paises[j]
                lista_paises[j] = aux
    return lista_paises

# === Calcular y mostrar estadísticas ===


def mostrar_estadisticas(lista_paises: list):
    if not lista_paises:
        print("No hay países cargados.")
        return

    pais_mayor_pob = lista_paises[0]
    pais_menor_pob = lista_paises[0]
    total_poblacion = 0
    total_superficie = 0

    for p in lista_paises:
        total_poblacion += p.poblacion
        total_superficie += p.superficie

        if p.poblacion > pais_mayor_pob.poblacion:
            pais_mayor_pob = p
        if p.poblacion < pais_menor_pob.poblacion:
            pais_menor_pob = p

    promedio_pob = total_poblacion / len(lista_paises)
    promedio_sup = total_superficie / len(lista_paises)

    paises_por_continente = {}
    for p in lista_paises:
        cont = p.continente
        if cont not in paises_por_continente:
            paises_por_continente[cont] = 1
        else:
            paises_por_continente[cont] += 1

    print("\n=== ESTADÍSTICAS GENERALES ===")
    print(
        f"País con mayor población: {pais_mayor_pob.nombre} ({pais_mayor_pob.poblacion:,} hab.)")
    print(
        f"País con menor población: {pais_menor_pob.nombre} ({pais_menor_pob.poblacion:,} hab.)")
    print(f"Promedio de población: {promedio_pob:,.0f}")
    print(f"Promedio de superficie: {promedio_sup:,.0f} km²")
    print("Cantidad de países por continente:")
    for cont, cant in paises_por_continente.items():
        print(f"   - {cont}: {cant}")

# === Agregar un nuevo país ===


def agregar_pais(lista_paises: list, dicc_paises: dict, ruta_csv: str):
    while True:
        print("\n=== AGREGAR NUEVO PAÍS ===")
        print("(Escriba 0 para cancelar)")

        nombre = input("Nombre del país: ").strip()
        if nombre == "0":
            print("Operación cancelada.")
            return
        if nombre == "":
            print("Ingrese un nombre válido.")
            continue
        existe = any(Paisdelmundo.quitar_acentos(p.nombre.lower()) ==
                     Paisdelmundo.quitar_acentos(nombre.lower()) for p in lista_paises)
        if existe:
            print("Ese país ya existe.")
            continue
        nombre = nombre.capitalize()

        while True:
            poblacion_str = input("Población: ").strip()
            if poblacion_str == "0":
                print("Operación cancelada.")
                return
            if not poblacion_str.isdigit():
                print("Ingrese solo números.")
                continue
            poblacion = int(poblacion_str)
            break

        while True:
            superficie_str = input("Superficie en km²: ").strip()
            if superficie_str == "0":
                print("Operación cancelada.")
                return
            if not superficie_str.isdigit():
                print("Ingrese solo números.")
                continue
            superficie = int(superficie_str)
            break

        # --- Detección y corrección automática de acentos en continentes ---
        continentes_validos = {
            "america": "América",
            "africa": "África",
            "europa": "Europa",
            "asia": "Asia",
            "oceania": "Oceanía",
            "antartida": "Antártida"
        }

        continente = input("Continente: ").strip().lower()
        if continente == "0":
            print("Operación cancelada.")
            return

        continente_sin_acentos = Paisdelmundo.quitar_acentos(continente)
        continente_final = continentes_validos.get(
            continente_sin_acentos, continente.capitalize())

        if dicc_paises:
            nuevo_codigo = max(dicc_paises.keys()) + 1
        else:
            nuevo_codigo = 1

        nuevo_pais = Paisdelmundo(
            nuevo_codigo, nombre, poblacion, superficie, continente_final)
        lista_paises.append(nuevo_pais)
        dicc_paises[nuevo_codigo] = nuevo_pais

        try:
            with open(
                    ruta_csv, "a", encoding="utf-8") as archivo:
                archivo.write(
                    f"\n{nuevo_codigo},{nombre},{poblacion},{superficie},{continente_final}")
            print(
                f"\nPaís '{nombre}' agregado con éxito (código: {nuevo_codigo}, continente: {continente_final})")
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

        # Pregunta si desea agregar otro país
        continuar = input(
            "\n¿Desea agregar otro país? (s/n): ").strip().lower()
        if continuar != "s":
            print("Volviendo al menú principal...")
            break


# === Programa principal con menú ===
if __name__ == "__main__":
    lista_paises, dicc_paises = Paisdelmundo.cargar_datos_csv(ruta_csv)

    if lista_paises:
        print(f"\nSe cargaron {len(lista_paises)} países correctamente.\n")

        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Mostrar todos los países")
            print("2. Buscar país por nombre")
            print("3. Filtrar países")
            print("4. Ordenar países")
            print("5. Mostrar estadísticas")
            print("6. Agregar país")
            print("0. Salir")

            opcion = input("Elija una opción: ").strip()

            if opcion == "1":
                Paisdelmundo.mostrar_todos_los_paises(lista_paises)
            elif opcion == "2":
                Paisdelmundo.buscar_pais(lista_paises)
            elif opcion == "3":
                filtrar_paises(lista_paises)
            elif opcion == "4":
                print("1. Ordenar por nombre")
                print("2. Ordenar por población")
                print("3. Ordenar por superficie")
                print("0. Volver")
                sub = input("Elija una opción: ").strip()
                if sub == "1":
                    Paisdelmundo.mostrar_todos_los_paises(
                        ordenar_paises_por_nombre(lista_paises))
                elif sub == "2":
                    Paisdelmundo.mostrar_todos_los_paises(
                        ordenar_paises_por_poblacion(lista_paises))
                elif sub == "3":
                    Paisdelmundo.mostrar_todos_los_paises(
                        ordenar_paises_por_superficie(lista_paises))
            elif opcion == "5":
                mostrar_estadisticas(lista_paises)
            elif opcion == "6":
                agregar_pais(lista_paises, dicc_paises,
                             ruta_csv)
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
    else:
        print("No se pudieron cargar los países.")
