class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.ci = ci

    def mostrar(self):
        print(f"{self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} - CI: {self.ci}")


class Niño(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci, edad, peso, talla):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, ci)
        self.edad = edad
        self.peso = float(peso)
        self.talla = float(talla)

    def mostrar(self):
        super().mostrar()
        print(f"Edad: {self.edad}, Peso: {self.peso} kg, Talla: {self.talla} m\n")


class ArchNiño:
    def __init__(self):
        self.lista = []

    def agregar(self, niño):
        self.lista.append(niño)

    def listar(self):
        for niño in self.lista:
            niño.mostrar()

    def peso_adecuado(self, niño):
        peso_min = 2 * niño.edad + 8
        peso_max = 3 * niño.edad + 12
        return peso_min <= niño.peso <= peso_max

    def contar_peso_adecuado(self):
        return sum(1 for n in self.lista if self.peso_adecuado(n))

    def listar_inadecuados(self):
        print("Niños con peso fuera de lo recomendado:")
        for n in self.lista:
            if not self.peso_adecuado(n):
                n.mostrar()

    def promedio_edad(self):
        if not self.lista:
            return 0
        return sum(n.edad for n in self.lista) / len(self.lista)

    def buscar_por_ci(self, ci):
        for n in self.lista:
            if n.ci == ci:
                return n
        return None

    def mayores_talla(self):
        if not self.lista:
            return []
        max_talla = max(n.talla for n in self.lista)
        return [n for n in self.lista if n.talla == max_talla]
arch = ArchNiño()

arch.agregar(Niño("Ana", "Rojas", "Lopez", 101, 7, 22, 1.20))
arch.agregar(Niño("Luis", "Perez", "Gomez", 102, 8, 30, 1.28))
arch.agregar(Niño("Mia", "Vargas", "Flores", 103, 7, 17, 1.10))

print("=== Listado ===")
arch.listar()

print("Niños con peso adecuado:", arch.contar_peso_adecuado())

print("\n=== Niños inadecuados ===")
arch.listar_inadecuados()

print("\nPromedio de edad:", arch.promedio_edad())

print("\n=== Buscar niño con CI 102 ===")
n = arch.buscar_por_ci(102)
if n:
    n.mostrar()

print("\n=== Niños con mayor talla ===")
for n in arch.mayores_talla():
    n.mostrar()
