class Animal:
    def __init__(self, especie, nombre, cantidad):
        self.especie = especie
        self.nombre = nombre
        self.cantidad = cantidad

class Zoologico:
    MAX_ANIMALES = 30

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.animales = []  
        self.noAnimales = 0

    def agregar_animal(self, animal):
        if len(self.animales) < self.MAX_ANIMALES:
            self.animales.append(animal)
            self.noAnimales += 1

    def eliminar_animales(self):
        self.animales = []
        self.noAnimales = 0


class ArchZoo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.zoologicos = []

    def crear(self, zoologico):
        self.zoologicos.append(zoologico)

    def modificar(self, id, nuevoNombre=None):
        for z in self.zoologicos:
            if z.id == id:
                if nuevoNombre:
                    z.nombre = nuevoNombre
                return True
        return False

    def eliminar(self, id):
        for z in self.zoologicos:
            if z.id == id:
                self.zoologicos.remove(z)
                return True
        return False

    def zoologicos_con_mas_animales(self):
        if not self.zoologicos:
            return []

        max_cantidad = max(z.noAnimales for z in self.zoologicos)
        return [z for z in self.zoologicos if z.noAnimales == max_cantidad]

    def eliminar_vacios(self):
        vacios = [z for z in self.zoologicos if z.noAnimales == 0]
        self.zoologicos = [z for z in self.zoologicos if z.noAnimales > 0]
        return vacios

    def animales_de_especie(self, especie):
        resultado = []
        for z in self.zoologicos:
            for a in z.animales:
                if a.especie == especie:
                    resultado.append((z.nombre, a))
        return resultado

    def mover_animales(self, id_origen, id_destino):
        zoo_origen = next((z for z in self.zoologicos if z.id == id_origen), None)
        zoo_destino = next((z for z in self.zoologicos if z.id == id_destino), None)

        if not zoo_origen or not zoo_destino:
            return False

        for a in zoo_origen.animales:
            zoo_destino.agregar_animal(a)

        zoo_origen.eliminar_animales()

        return True


if __name__ == "__main__":
    arch = ArchZoo("Archivo principal")

    z1 = Zoologico(1, "Zoo Norte")
    z2 = Zoologico(2, "Zoo Sur")
    z3 = Zoologico(3, "Zoo Este")

    arch.crear(z1)
    arch.crear(z2)
    arch.crear(z3)

    z1.agregar_animal(Animal("Felino", "Tigre", 2))
    z1.agregar_animal(Animal("Ave", "Cóndor", 1))

    z2.agregar_animal(Animal("Felino", "León", 3))

    print("\nb) Zoológicos con más animales:")
    for z in arch.zoologicos_con_mas_animales():
        print(z.nombre)

    vacios = arch.eliminar_vacios()
    print("\nc) Zoológicos eliminados por estar vacíos:")
    for z in vacios:
        print(z.nombre)

    print("\nd) Animales de especie Felino:")
    for nombre_zoo, animal in arch.animales_de_especie("Felino"):
        print(f"{animal.nombre} en {nombre_zoo}")

    arch.mover_animales(1, 2)

    print("\nDespués de mover animales, animales del Zoo Sur:")
    for a in z2.animales:
        print(a.nombre, "-", a.especie)
