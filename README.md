### Descripción del Proyecto:

Este proyecto es un programa desarrollado en Python que permite gestionar información de países mediante la lectura y escritura de un archivo CSV.
El sistema aplica conceptos de Programación Orientada a Objetos (POO) y estructuras de datos como listas y diccionarios, ofreciendo un menú interactivo para que el usuario pueda:

Mostrar, buscar, ordenar y filtrar países.

Calcular estadísticas generales.

Agregar nuevos países con validaciones automáticas.

El trabajo integra los contenidos vistos en la materia, aplicando la lógica de programación, validación de datos, uso de clases, métodos y manejo de archivos.

### Datos institucionales

Universidad: Universidad Tecnológica Nacional (UTN).
Facultad Regional: [Facultad Regional Mendoza (UTN FRM)].
Carrera: Tecnicatura Universitaria en Programación.
Asignatura: Programación I.
Año lectivo: 2025 – 2° Cuatrimestre.
Comisión: 1.
Docente: Magni Negri, Gerardo Luis.

Integrantes del grupo:

Mariano Chirino.



### Estructura:

El proyecto se desarrolló en equipo, organizando el trabajo por etapas y dividiendo las responsabilidades entre los integrantes.
Cada miembro del grupo trabajó en su propia rama de desarrollo, aportando funciones específicas como la lectura del archivo CSV, la creación del menú principal, la búsqueda de países, los filtros, las estadísticas y la funcionalidad de agregar nuevos registros.

Una vez completadas las partes individuales, se realizó la integración final en un único archivo Python, verificando el correcto funcionamiento general y la coherencia entre las validaciones, el menú y las estructuras de datos.

### Instrucciones de ejecución:

Para ejecutar el programa correctamente:

Descargar o clonar la carpeta del proyecto completa, asegurándose de que el archivo
integrador_primer_semestre.py y paises.csv estén en la misma carpeta.

Opción 1 – Desde Visual Studio Code (VS Code):

Abrir la carpeta del proyecto en VS Code.

Seleccionar el archivo integrador_primer_semestre.py.

Presionar el botón “Run Python File” (ícono ▶️ en la esquina superior derecha).

El menú principal aparecerá en la consola integrada.

Opción 2 – Windows (CMD Y POWERSHELL)

Para ejecutar el programa correctamente, asegurarse de tener instalada una versión de Python 3.10 o superior y de que el archivo paises.csv se encuentre en la misma carpeta que integrador_primer_semestre.py.

1.Windows (CMD)

Abrir el Símbolo del sistema (CMD).

Navegar hasta la carpeta donde se encuentra el proyecto:

cd Ruta\hasta\la\carpeta\del\proyecto

Ejecutar el programa:

python integrador_primer_semestre.py

2. Windows (PowerShell)

Abrir PowerShell.

Cambiar al directorio del proyecto:

cd "C:\Ruta\hasta\la\carpeta\del\proyecto"

Ejecutar el programa:
python .\integrador_primer_semestre.py

Si ese comando no funcionara:

py .\integrador_primer_semestre.py


Opción 3 – Linux (Ubuntu, Debian, etc.)

Abrir una terminal.

Ir al directorio del proyecto:

cd /ruta/hasta/la/carpeta/proyecto

Ejecutar el programa:
python3 integrador_primer_semestre.py

4. macOS –

Abrir la Terminal.

Navegar a la carpeta donde está el archivo:

cd /Users/tu_usuario/Documentos/proyecto

Ejecutar el programa:

python3 integrador_primer_semestre.py

Recomendaciones generales

Asegurarse de que el archivo paises.csv esté en la misma carpeta que el programa.

En caso de error “python no reconocido”, verificar que Python esté instalado y agregado al PATH.

Para salir del programa, seleccionar la opción 0 en el menú principal.

### Librerias:

import csv 
csv es parte de la librería estándar de Python, cualquier persona que tenga Python instalado (de la versión correcta) podrá ejecutar el proyecto sin necesidad de instalar nada adicional.

La versión mínima de Python que se necesita, por ejemplo: Python 3.10+.

Link a repositorio de GitHub: https://github.com/marianoemir/tpi-utn-frm-programacion1  
Link a Video del Proyecto: 


### Ejemplos de entrada y salida:

Archivo de entrada (paises.csv)

codigo,nombre,poblacion,superficie,continente
1,Argentina,45376763,2780400,América
2,Brasil,213993437,8515767,América
3,Alemania,83149300,357022,Europa
4,Egipto,104000000,1002450,África
5,Australia,25690000,7692000,Oceanía
6,China,1412000000,9596960,Asia
7,India,1393000000,3287263,Asia
8,Canadá,38000000,9984670,América
9,España,47450795,505990,Europa
10,Argelia,47400000,2381741,África

1. Búsqueda parcial de país

=== MENÚ PRINCIPAL ===
2
=== BUSCAR PAÍS POR NOMBRE ===
1. Búsqueda exacta (nombre completo)
2. Búsqueda parcial (parte del nombre)
0. Volver al menú principal
Elija una opción: 2 
Ingrese parte del nombre del país: an

Se encontraron 2 coincidencias:
3 - Alemania | Pob: 83,149,300 | Sup: 357,022 km² | Europa
8 - Canadá | Pob: 38,000,000 | Sup: 9,984,670 km² | América


2. Agregar un nuevo país

Entrada:

=== MENÚ PRINCIPAL ===
6
=== AGREGAR NUEVO PAÍS ===
(Escriba 0 y ENTER para cancelar en cualquier paso)
Nombre del país: Chile
Población (solo números): 19107216
Superficie en km² (solo números): 756102
Continente: América

Salida:
País 'Chile' agregado con éxito (código: 11)

El archivo paises.csv se actualiza con:
11,Chile,19107216,756102,América

3. Mostrar estadísticas generales

Entrada:
=== MENÚ PRINCIPAL ===
5

Salida:
ESTADÍSTICAS GENERALES
País con mayor población: China (1,412,000,000 hab.)
País con menor población: Australia (25,690,000 hab.)
Promedio de población: 374,949,131
Promedio de superficie: 5,337,717 km²
Cantidad de países por continente:
   - América: 3
   - Europa: 2
   - África: 2
   - Oceanía: 1
   - Asia: 2

4. Ordenar países por población

Entrada:

=== MENÚ PRINCIPAL ===
4
Seleccione una opcion para ordenar los paises:
1.Ordenar por nombre
2.Ordenar por poblacion
3.Ordenar por superficie
0.Salir
Elija una opcion: 2

Salida (parcial):

LISTA COMPLETA DE PAiSES:

5 - Australia | Pob: 25,690,000 | Sup: 7,692,000 km² | Oceanía
8 - Canadá | Pob: 38,000,000 | Sup: 9,984,670 km² | América
1 - Argentina | Pob: 45,376,763 | Sup: 2,780,400 km² | América
10 - Argelia | Pob: 47,400,000 | Sup: 2,381,741 km² | África
9 - España | Pob: 47,450,795 | Sup: 505,990 km² | Europa
3 - Alemania | Pob: 83,149,300 | Sup: 357,022 km² | Europa
4 - Egipto | Pob: 104,000,000 | Sup: 1,002,450 km² | África
2 - Brasil | Pob: 213,993,437 | Sup: 8,515,767 km² | América
7 - India | Pob: 1,393,000,000 | Sup: 3,287,263 km² | Asia
6 - China | Pob: 1,412,000,000 | Sup: 9,596,960 km² | Asia

Total de paises: 10

5. Filtrar países por continente

Entrada:
=== MENÚ PRINCIPAL ===
3
=== FILTRAR PAÍSES ===
1. Por continente
2. Por rango de población
3. Por rango de superficie
0. Volver al menú principal
Elija una opción: 1
Ingrese el nombre del continente: asia

Salida:
Países en el continente 'Asia':

6 - China | Pob: 1,412,000,000 | Sup: 9,596,960 km² | Asia
7 - India | Pob: 1,393,000,000 | Sup: 3,287,263 km² | Asia

Total: 2 país(es)


**Trabajo integrador final - Programación I (UTN FRM, 2025)**  
Proyecto desarrollado con Python 3.10+ aplicando Programación Orientada a Objetos (POO).
