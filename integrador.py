 
#esta funcion calcula y muestra las estadisticas

def mostrar_estadisticas(lista_paises:list) :
  if not lista_paises:
    print("no hay paises cargados")
    return 
  
  #inicializamos variables para la mayor y menor poblacion 

  paises_mayor_poblacion = lista_paises[0]
  paises_menor_poblacion = lista_paises[0]
  total_poblacion= 0
  total_superficie=0

  for p in lista_paises:
    total_poblacion+= p.poblacion 
    total_superficie+= p.superficie


    if p.poblacion > pais_mayor_pob.poblacion:
      pais_mayor_pob = p

    if p.poblacion < pais_menor_pob.poblacion :
      pais_menor_pob= p
       

    promedio_pob = total_poblacion / len(lista_paises)
    promedio_sup = total_superficie / len(lista_paises)


    # Contar países por continente
    paises_por_continente = {}
    for p in lista_paises:
        cont = p.continente
        if cont not in paises_por_continente:
            paises_por_continente[cont] = 1
        else:
            paises_por_continente[cont] += 1

print("\n📊 ESTADÍSTICAS GENERALES 📊")
print(f"➡ País con mayor población: {pais_mayor_pob.nombre} ({pais_mayor_pob.poblacion:,} hab.)")
print(f"➡ País con menor población: {pais_menor_pob.nombre} ({pais_menor_pob.poblacion:,} hab.)")
print(f"➡ Promedio de población: {promedio_pob:,.0f}")
print(f"➡ Promedio de superficie: {promedio_sup:,.0f} km²")
print("➡ Cantidad de países por continente:")
for cont, cant in paises_por_continente.items():
        print(f"   - {cont}: {cant}")


