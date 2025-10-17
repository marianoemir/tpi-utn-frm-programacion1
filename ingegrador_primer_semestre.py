import csv    #Sirve para leer archivos CSV (valores separados por comas)

# Creamos una clase llamada Paises
# Esta clase nos permite guardar toda la información de cada país de forma ordenada.

class Paisdelmundo:

    # El método __init__ se ejecuta automáticamente cada vez que creamos un nuevo país.
    def __init__(self, codigo: int, nombre: str, poblacion: int, superficie: int, continente: str):
        # Guardamos los datos del país dentro del objeto
        self.codigo = codigo
        self.nombre = nombre
        self.poblacion = poblacion
        self.superficie = superficie
        self.continente = continente

    # Este metodo sirve para mostrar el pais en texto cuando usamos "print(pais)"
    def __str__(self):
        # {:,} pone comas en los números grandes (ejemplo: 45,376,763)
        return f"{self.codigo} - {self.nombre} | Pob: {self.poblacion:,} | Sup: {self.superficie:,} km² | {self.continente}"

    # Este metodo convierte el pais en un diccionario (util si luego queremos guardar en CSV)
    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "superficie": self.superficie,
            "continente": self.continente
        }


# Definimos una funcion para leer el archivo CSV
def cargar_datos_csv(ruta_csv: str):
    """
    Esta función lee el archivo CSV (por ejemplo: paises.csv)
    y devuelve dos cosas:
    - una lista de objetos paises (uno por cada país)
    - un diccionario que usa el 'codigo' como clave
    """

    # Creamos estructuras vacias para guardar los paises
    lista_paises = []      # para recorrerlos o mostrar varios
    dicc_por_codigo = {}   # para buscar rápido por código

    try:
        # Abrimos el archivo CSV con codificación UTF-8 (para que lea acentos correctamente)
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            # Usamos DictReader para leer cada fila como un diccionario
            lector = csv.DictReader(archivo)

            # Recorremos cada fila del archivo
            for fila in lector:
                try:
                    # Convertimos los datos de texto a su tipo correcto
                    codigo = int(fila["codigo"])              # el codigo debe ser un numero entero
                    nombre = fila["nombre"].strip()           # quitamos espacios en blanco al principio y final
                    poblacion = int(fila["poblacion"])        # convertimos el texto a número entero
                    superficie = int(fila["superficie"])
                    continente = fila["continente"].strip()

                    # Validamos que el codigo no esté repetido
                    if codigo in dicc_por_codigo:
                        print(f"Código duplicado ({codigo}) para {nombre}, se omite.")
                        continue  # salta al siguiente país

                    # Creamos el objeto Country con los datos leidos
                    pais = Paisdelmundo(codigo, nombre, poblacion, superficie, continente)

                    # Agregamos el pais a la lista
                    lista_paises.append(pais)

                    # También lo guardamos en el diccionario (clave = codigo)
                    dicc_por_codigo[codigo] = pais

                except Exception as e:
                    # Si hay error en esa fila (por ejemplo un dato vacío o texto donde debería haber un numero)
                    print(f"Error al procesar fila: {fila} ({e})")

        # Cuando terminamos de leer todo, mostramos cuantos países se cargaron
        print(f"Se cargaron {len(lista_paises)} países desde {ruta_csv}")

        # Devolvemos los datos para usarlos en el programa
        return lista_paises, dicc_por_codigo

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
        return [], {}

if __name__ == "__main__": 
    lista_paises, dicc_paises = cargar_datos_csv("paises.csv") 
print("\nPrimeros países cargados:\n") 
for pais in lista_paises: 
    print(pais)


"""Estructura Principal del programa.
if __name__ == "__main__":
    # Cargamos los datos del CSV
    lista_paises, dicc_paises = cargar_datos_csv("paises.csv")

    # Verificamos que se hayan cargado correctamente
    if lista_paises:
        print(f"\nSe cargaron {len(lista_paises)} países correctamente.\n")
        
        # Acá empieza el menú principal
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Mostrar todos los países")
            print("2. Buscar país por código")
            print("3. Filtrar por continente")
            print("0. Salir")

            opcion = input("Elija una opción: ").strip()

            if opcion == "1":
                for p in lista_paises:
                    print(p)

            elif opcion == "2":
                codigo = input("Ingrese el codigo del país: ")
                if codigo.isdigit() and int(codigo) in dicc_paises:
                    print(dicc_paises[int(codigo)])
                else:
                    print("Código invalido o no encontrado.")

            elif opcion == "3":
                print("Funcion pendiente (filtrar por continente).")

            elif opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("La Opcion no valida.")
    else:
        print("No se pudieron cargar los países.")"""
