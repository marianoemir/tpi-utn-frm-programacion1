import csv  # Para leer archivos CSV

# === Clase principal que representa un país ===
class Paisdelmundo:
    def __init__(self, codigo: int, nombre: str, poblacion: int, superficie: int, continente: str):
        self.codigo = codigo
        self.nombre = nombre
        self.poblacion = int(poblacion)
        self.superficie = int(superficie)
        self.continente = continente

    def __str__(self):
        return f"{self.codigo} - {self.nombre} | Pob: {self.poblacion:,} | Sup: {self.superficie:,} km² | {self.continente}"

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "superficie": self.superficie,
            "continente": self.continente
        }

# === Función auxiliar para eliminar acentos ===
def quitar_acentos(texto: str):
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"),
        ("ó", "o"), ("ú", "u"),
        ("Á", "A"), ("É", "E"), ("Í", "I"),
        ("Ó", "O"), ("Ú", "U")
    )
    for a, b in reemplazos:
        texto = texto.replace(a, b)
    return texto

# === Leer el archivo CSV y crear estructuras ===
def cargar_datos_csv(ruta_csv: str):
    lista_paises = []
    dicc_por_codigo = {}

    try:
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    codigo = int(fila["codigo"])
                    nombre = fila["nombre"].strip()
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                    continente = fila["continente"].strip()

                    if codigo in dicc_por_codigo:
                        print(f"Código duplicado ({codigo}) para {nombre}, se omite.")
                        continue

                    pais = Paisdelmundo(codigo, nombre, poblacion, superficie, continente)
                    lista_paises.append(pais)
                    dicc_por_codigo[codigo] = pais

                except Exception as e:
                    print(f"Error al procesar fila: {fila} ({e})")

        print(f"Se cargaron {len(lista_paises)} países desde {ruta_csv}")
        return lista_paises, dicc_por_codigo

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
        return [], {}

# === Mostrar todos los países cargados ===
def mostrar_todos_los_paises(lista_paises: list):
    if not lista_paises:
        print("No hay países cargados.")
        return

    print("\nLISTA COMPLETA DE PAÍSES:\n")
    for pais in lista_paises:
        print(pais)
    print(f"\nTotal de países: {len(lista_paises)}")

# === Buscar país por nombre (exacto o parcial) ===
def buscar_pais_por_nombre(lista_paises: list):
    if not lista_paises:
        print("No hay países cargados.")
        return

    while True:
        print("\n=== BUSCAR PAÍS POR NOMBRE ===")
        print("1. Búsqueda exacta")
        print("2. Búsqueda parcial")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ").strip()

        if opcion == "0":
            break

        elif opcion == "1":
            nombre_buscar = input("Ingrese el nombre exacto: ").strip().lower()
            if not nombre_buscar:
                print("Ingrese un nombre válido.")
                continue

            encontrado = False
            for p in lista_paises:
                if quitar_acentos(p.nombre.lower()) == quitar_acentos(nombre_buscar):
                    print(f"\nPaís encontrado:\n{p}")
                    encontrado = True
                    break

            if not encontrado:
                print(f"No se encontró '{nombre_buscar.capitalize()}'.")

        elif opcion == "2":
            fragmento = input("Ingrese parte del nombre: ").strip().lower()
            if not fragmento:
                print("Ingrese al menos una letra.")
                continue

            resultados = []
            for p in lista_paises:
                if quitar_acentos(fragmento) in quitar_acentos(p.nombre.lower()):
                    resultados.append(p)

            if resultados:
                print(f"\nSe encontraron {len(resultados)} coincidencias:")
                for pais in resultados:
                    print(pais)
            else:
                print("No se encontraron coincidencias.")
        else:
            print("Opción no válida.")

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
            continente = input("Ingrese el nombre del continente: ").strip().lower()
            resultados = [p for p in lista_paises if quitar_acentos(p.continente.lower()) == quitar_acentos(continente)]
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
            resultados = [p for p in lista_paises if minimo <= p.poblacion <= maximo]
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
            resultados = [p for p in lista_paises if minimo <= p.superficie <= maximo]
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
    print(f"País con mayor población: {pais_mayor_pob.nombre} ({pais_mayor_pob.poblacion:,} hab.)")
    print(f"País con menor población: {pais_menor_pob.nombre} ({pais_menor_pob.poblacion:,} hab.)")
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
        existe = any(quitar_acentos(p.nombre.lower()) == quitar_acentos(nombre.lower()) for p in lista_paises)
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

        continente = input("Continente: ").strip().capitalize()
        if continente == "0":
            print("Operación cancelada.")
            return

        if dicc_paises:
            nuevo_codigo = max(dicc_paises.keys()) + 1
        else:
            nuevo_codigo = 1

        nuevo_pais = Paisdelmundo(nuevo_codigo, nombre, poblacion, superficie, continente)
        lista_paises.append(nuevo_pais)
        dicc_paises[nuevo_codigo] = nuevo_pais

        try:
            with open(ruta_csv, "a", encoding="utf-8") as archivo:
                archivo.write(f"\n{nuevo_codigo},{nombre},{poblacion},{superficie},{continente}")
            print(f"\nPaís '{nombre}' agregado con éxito (código: {nuevo_codigo})")
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

        
        continuar = input("\n¿Desea agregar otro país? (s/n): ").strip().lower()
        if continuar != "s":
            print("Volviendo al menú principal...")
            break

# === Programa principal con menú ===
if __name__ == "__main__":
    lista_paises, dicc_paises = cargar_datos_csv("paises.csv")

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
                mostrar_todos_los_paises(lista_paises)
            elif opcion == "2":
                buscar_pais_por_nombre(lista_paises)
            elif opcion == "3":
                filtrar_paises(lista_paises)
            elif opcion == "4":
                print("1. Ordenar por nombre")
                print("2. Ordenar por población")
                print("3. Ordenar por superficie")
                print("0. Volver")
                sub = input("Elija una opción: ").strip()
                if sub == "1":
                    mostrar_todos_los_paises(ordenar_paises_por_nombre(lista_paises))
                elif sub == "2":
                    mostrar_todos_los_paises(ordenar_paises_por_poblacion(lista_paises))
                elif sub == "3":
                    mostrar_todos_los_paises(ordenar_paises_por_superficie(lista_paises))
            elif opcion == "5":
                mostrar_estadisticas(lista_paises)
            elif opcion == "6":
                agregar_pais(lista_paises, dicc_paises, "paises.csv")
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
    else:
        print("No se pudieron cargar los países.")
