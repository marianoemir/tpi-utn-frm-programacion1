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
    pass