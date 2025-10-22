import csv    #Sirve para leer archivos CSV (valores separados por comas)

# Creamos una clase llamada Paises
# Esta clase nos permite guardar toda la información de cada país de forma ordenada.

class Paisdelmundo:

    # El método __init__ se ejecuta automaticamente cada vez que creamos un nuevo pais.
    def __init__(self, codigo: int, nombre: str, poblacion: int, superficie: int, continente: str):
        # Guardamos los datos del pais dentro del objeto
        self.codigo = codigo
        self.nombre = nombre
        self.poblacion = int(poblacion)
        self.superficie = int(superficie)
        self.continente = continente
        

    # Este metodo sirve para mostrar el pais en texto cuando usamos "print(pais)"
    def __str__(self):
        # {:,} pone comas en los numeros grandes (ejemplo: 45,376,763)
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
        print("No se encontro el archivo CSV.")
        return [], {}



def mostrar_todos_los_paises(lista_paises: list):
    """
    Muestra en pantalla todos los paises cargados en la lista.
    Recibe por parametro la lista de objetos Paisdelmundo.
    """

    if not lista_paises:
        print("No hay paises cargados.")
        return

    print("\nLISTA COMPLETA DE PAiSES:\n")

    # Recorremos la lista y mostramos cada país usando __str__()
    for pais in lista_paises:
        print(pais)

    print(f"\nTotal de paises: {len(lista_paises)}")
#creamos una funcion para ordenar los paises por nombre

def ordenar_paises_por_nombre(lista_paises: list):
    #recibe por parametro la lista de objetos Paisdelmundo
    #creamos un bucle para ordenar los paises si el nombre del pais es mayor al siguiente usamos una variable auxiliar
    #para ir guardando el pais y luego ir intercambiando las posiciones
    for i in range(len(lista_paises)):
        for j in range(i+1, len(lista_paises)):
            if lista_paises[i].nombre > lista_paises[j].nombre:
                aux= lista_paises[i] 
                lista_paises[i]= lista_paises[j]
                lista_paises[j]= aux
    return lista_paises

#creamos una funcion para ordenar los paises por poblacion
def ordenar_paises_por_poblacion(lista_paises: list):
    for i in range(len(lista_paises)):
        for j in range(i+1, len(lista_paises)):
            if lista_paises[i].poblacion > lista_paises[j].poblacion:
                aux= lista_paises[i] 
                lista_paises[i]= lista_paises[j]
                lista_paises[j]= aux
    return lista_paises


def ordenar_paises_por_superficie(lista_paises: list):
    for i in range(len(lista_paises)):
        for j in range(i+1, len(lista_paises)):
            if lista_paises[i].superficie > lista_paises[j].superficie:
                aux = lista_paises[i]
                lista_paises[i]= lista_paises[j]
                lista_paises[j]= aux
    return lista_paises


#esta funcion calcula y muestra las estadisticas  

def mostrar_estadisticas(lista_paises:list) :
  if not lista_paises:
    print("no hay paises cargados")
    return 
  
  #inicializamos variables para la mayor y menor poblacion 

  pais_mayor_pob= lista_paises[0]
  pais_menor_pob = lista_paises[0]
  total_poblacion= 0
  total_superficie=0

    #Recorremos la lista
  for p in lista_paises:
    total_poblacion+= p.poblacion 
    total_superficie+= p.superficie


    if p.poblacion > pais_mayor_pob.poblacion:
      pais_mayor_pob = p

    if p.poblacion < pais_menor_pob.poblacion :
      pais_menor_pob= p
       

  promedio_pob = total_poblacion / len(lista_paises)
  promedio_sup = total_superficie / len(lista_paises)


    #Contar países por continente
  paises_por_continente = {}
  for p in lista_paises: 
        cont = p.continente
        if cont not in paises_por_continente:
            paises_por_continente[cont] = 1
        else:
            paises_por_continente[cont] += 1

  print("\n ESTADÍSTICAS GENERALES ")
  print(f"País con mayor población: {pais_mayor_pob.nombre} ({pais_mayor_pob.poblacion:,} hab.)")
  print(f"País con menor población: {pais_menor_pob.nombre} ({pais_menor_pob.poblacion:,} hab.)")
  print(f"Promedio de población: {promedio_pob:,.0f}")
  print(f"Promedio de superficie: {promedio_sup:,.0f} km²")
  print("Cantidad de países por continente:")
  for cont, cant in paises_por_continente.items():
        print(f"   - {cont}: {cant}")



def agregar_pais(lista_paises: list, dicc_paises: dict, ruta_csv: str):
    """
    Versión simple y segura de agregar_pais.
    Genera nuevo_codigo ANTES de escribir y maneja errores sin romper el programa.
    """

    print("\n=== AGREGAR NUEVO PAÍS ===")
    print("(Escriba 0 y ENTER para cancelar en cualquier paso)")

    #Nombre del Pais
    while True:
        nombre = input("Nombre del país: ").strip()
        if nombre == "0":
            print("Operación cancelada.")
            return
        if nombre == "":
            print("Por favor, ingrese un nombre válido.")
            continue
        # validar duplicado por nombre
        existe = any(p.nombre.lower() == nombre.lower() for p in lista_paises)
        if existe:
            print("Ese país ya existe. Intente con otro nombre o escriba 0 para cancelar.")
            continue
        nombre = nombre.capitalize()
        break

    #Poblacion del Pais
    while True:
        poblacion_str = input("Población (solo números): ").strip()
        if poblacion_str == "0":
            print("Operación cancelada.")
            return
        if not poblacion_str.isdigit():
            print("Ingrese solo números.")
            continue
        poblacion = int(poblacion_str)
        if poblacion <= 0:
            print("La población debe ser mayor a 0.")
            continue
        break

    #Superficie del Pais
    while True:
        superficie_str = input("Superficie en km² (solo números): ").strip()
        if superficie_str == "0":
            print("Operación cancelada.")
            return
        if not superficie_str.isdigit():
            print("Ingrese solo números.")
            continue
        superficie = int(superficie_str)
        if superficie <= 0:
            print("La superficie debe ser mayor a 0.")
            continue
        break

    #Continente del Pais
    while True:
        continente = input("Continente: ").strip()
        if continente == "0":
            print("Operación cancelada.")
            return
        if continente == "":
            print("Por favor, ingrese un continente válido.")
            continue
        continente = continente.capitalize()
        break

    #Genera el codigo antes de escribir
    if dicc_paises:
        try:
            nuevo_codigo = max(dicc_paises.keys()) + 1
        except Exception:
            # por si las claves no son enteros (caso raro)
            claves_int = [int(k) for k in dicc_paises.keys()]
            nuevo_codigo = max(claves_int) + 1
    else:
        nuevo_codigo = 1

    #Crear el objeto y agregar en memoria
    nuevo_pais = Paisdelmundo(nuevo_codigo, nombre, poblacion, superficie, continente)
    lista_paises.append(nuevo_pais)
    dicc_paises[nuevo_codigo] = nuevo_pais
    guardado_en_memoria = True  #marca que ya lo pusimos en memoria

    #Intentar escribir en el CSV (versión simple que añade newline para evitar "pegado")
    try:
        with open(ruta_csv, "a", encoding="utf-8") as archivo:
            #siempre escribimos un salto de linea primero para separar del último registro
            archivo.write(f"\n{nuevo_codigo},{nombre},{poblacion},{superficie},{continente}")
        print(f"\nPaís '{nombre}' agregado con éxito (código: {nuevo_codigo})")
    except Exception as e:
        print(f"Error al guardar en el archivo: {e}")
        #si algo fallo al guardar en disco revertimos la inserción en memoria
        if guardado_en_memoria:
            #eliminamos el ultimo elemento de la lista si coincide con el que agregamos
            if lista_paises and lista_paises[-1].codigo == nuevo_codigo:
                lista_paises.pop()
            #sacamos del diccionario si esta
            if nuevo_codigo in dicc_paises:
                dicc_paises.pop(nuevo_codigo)
        print("Se revirtió la operación en memoria.")






#Estructura Principal del programa.
if __name__ == "__main__":
    # Cargamos los datos del CSV
    lista_paises, dicc_paises = cargar_datos_csv("paises.csv")

    # Verificamos que se hayan cargado correctamente
    if lista_paises:
        print(f"\nSe cargaron {len(lista_paises)} paises correctamente.\n")
        
        # Acá empieza el menu principal
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Mostrar todos los países.")
            print("2. Buscar por coincidencia o busqueda parcial.")
            print("3. Filtrar por continente.")
            print("4. Mostrar estadisticas.")
            print("5. Agregar un pais.")
            print("0. Salir.")

            opcion = input("Elija una opción: ").strip()

            if opcion == "1":
                mostrar_todos_los_paises(lista_paises)
            elif opcion == "2":
                pass

            elif opcion == "3":
                print("Seleccione una opcion para ordenar los paises: ")
                print("1.Ordenar por nombre")
                print("2.Ordenar por poblacion")
                print("3.Ordenar por superficie")
                print("0.Salir")
                otra_opcion= input("Elija una opcion: ").strip()
                if otra_opcion == "1":
                    lista_ordenada= ordenar_paises_por_nombre(lista_paises)
                    mostrar_todos_los_paises(lista_ordenada)
                elif otra_opcion == "2":
                    lista_ordenada= ordenar_paises_por_poblacion(lista_paises)
                    mostrar_todos_los_paises(lista_ordenada)
                elif otra_opcion == "3":
                    lista_ordenada= ordenar_paises_por_superficie(lista_paises)
                    mostrar_todos_los_paises(lista_ordenada)
                elif otra_opcion == "0":
                    print("Volviendo al menu principal...")
                    
            elif opcion == "4":
                estadistica= mostrar_estadisticas(lista_paises)
            
            elif opcion == "5":
                agregar_pais(lista_paises, dicc_paises, "paises.csv")

            elif opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("La Opcion no valida.")
    else:
        print("No se pudieron cargar los países.")
