class Pais:
    contador_codigos = 0
    def __init__(self, nombre, poblacion, superficie, continente):
        self.nombre = nombre
        self.poblacion = float(poblacion)
        self.superficie = float(superficie)
        self.continente = continente
        Pais.contador_codigos += 1   

        self.codigo = str(Pais.contador_codigos).zfill(3) 
        
Pais1 = Pais ("Argentina","47700000", "2780400", "América del Sur")
Pais2 = Pais ("Argelia", "47400000", "2381741", "África")
Pais3 = Pais ("Alemania", "84100000", "357022", "Europa")
Pais4 = Pais ("México", "131946900", "1964375", "América del Norte")
Pais5 = Pais ("Chile", "19860000", "756626", "América del Sur")

print(Pais4.codigo)
