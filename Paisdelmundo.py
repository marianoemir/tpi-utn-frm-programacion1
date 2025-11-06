import csv

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

    # === Método estático para quitar acentos ===
    @staticmethod
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

    # === Método de clase para cargar países desde CSV ===
    @classmethod
    def cargar_datos_csv(cls, ruta_csv: str):
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
                            print(
                                f"Código duplicado ({codigo}) para {nombre}, se omite.")
                            continue
                        pais = cls(codigo, nombre, poblacion,
                                   superficie, continente)
                        lista_paises.append(pais)
                        dicc_por_codigo[codigo] = pais
                    except Exception as e:
                        print(f"Error al procesar fila: {fila} ({e})")
            print(f"Se cargaron {len(lista_paises)} países desde {ruta_csv}")
            return lista_paises, dicc_por_codigo
        except FileNotFoundError:
            print("No se encontró el archivo CSV.")
            return [], {}

    # === Método estático para mostrar todos los países ===
    @staticmethod
    def mostrar_todos_los_paises(lista_paises: list):
        if not lista_paises:
            print("No hay países cargados.")
            return
        print("\nLISTA COMPLETA DE PAÍSES:\n")
        for pais in lista_paises:
            print(pais)
        print(f"\nTotal de países: {len(lista_paises)}")

    # === Método para buscar países por nombre o código ===
    @staticmethod
    def buscar_pais(lista_paises: list):
        if not lista_paises:
            print("No hay países cargados.")
            return
        while True:
            print("\n=== BUSCAR PAÍS ===")
            print("1. Búsqueda exacta (por nombre o código)")
            print("2. Búsqueda parcial (por nombre)")
            print("0. Volver al menú principal")
            opcion = input("Elija una opción: ").strip()
            if opcion == "0":
                break
            elif opcion == "1":
                while True:
                    print("\n--- BÚSQUEDA EXACTA ---")
                    print("1. Buscar por nombre")
                    print("2. Buscar por código")
                    print("0. Volver")
                    subop = input("Elija una opción: ").strip()
                    if subop == "0":
                        break
                    elif subop == "1":
                        nombre_buscar = input(
                            "Ingrese el nombre exacto del país (o 0 para salir): ").strip()
                        if nombre_buscar == "0":
                            break
                        if not nombre_buscar:
                            print("Ingrese un nombre válido.")
                            continue
                        encontrado = False
                        for p in lista_paises:
                            if Paisdelmundo.quitar_acentos(p.nombre.lower()) == Paisdelmundo.quitar_acentos(nombre_buscar.lower()):
                                print(f"\nPaís encontrado:\n{p}")
                                encontrado = True
                                break
                        if not encontrado:
                            print(
                                f"No se encontró '{nombre_buscar.capitalize()}'. Intente nuevamente.")
                    elif subop == "2":
                        while True:
                            codigo_str = input(
                                "Ingrese el código del país (o 0 para salir): ").strip()
                            if codigo_str == "0":
                                break
                            if not codigo_str.isdigit():
                                print("Debe ingresar un número válido.")
                                continue
                            codigo = int(codigo_str)
                            encontrado = False
                            for p in lista_paises:
                                if p.codigo == codigo:
                                    print(f"\nPaís encontrado:\n{p}")
                                    encontrado = True
                                    break
                            if encontrado:
                                break
                            else:
                                print(
                                    f"No se encontró ningún país con el código {codigo}. Intente nuevamente.")
                    else:
                        print("Opción no válida, intente nuevamente.")
            elif opcion == "2":
                fragmento = input(
                    "Ingrese parte del nombre (o 0 para salir): ").strip()
                if fragmento == "0":
                    continue
                if not fragmento:
                    print("Ingrese al menos una letra.")
                    continue
                resultados = []
                for p in lista_paises:
                    if Paisdelmundo.quitar_acentos(fragmento.lower()) in Paisdelmundo.quitar_acentos(p.nombre.lower()):
                        resultados.append(p)
                if resultados:
                    print(f"\nSe encontraron {len(resultados)} coincidencias:")
                    for pais in resultados:
                        print(pais)
                else:
                    print("No se encontraron coincidencias.")
            else:
                print("Opción no válida.")
