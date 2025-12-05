class Medicamento:
    def __init__(self, nombre, codMedicamento, tipo, precio):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo      
        self.precio = precio

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Bs {self.precio}"
class Farmacia:
    def __init__(self, nombreFarmacia, sucursal, direccion):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []  

    def agregar(self, medicamento: Medicamento):
        self.medicamentos.append(medicamento)

    def getSucursal(self):
        return self.sucursal

    def getDireccion(self):
        return self.direccion

    def mostrarMedicamentosTos(self):
        return [m for m in self.medicamentos if m.tipo.lower() == "tos"]

    def mostrarMedicamentosX(self, tipo):
        return [m for m in self.medicamentos if m.tipo.lower() == tipo.lower()]

    def buscaMedicamento(self, nombre):
        for m in self.medicamentos:
            if m.nombre.lower() == nombre.lower():
                return m
        return None

    def __str__(self):
        return f"Sucursal {self.sucursal} - {self.direccion}"
class ArchFarmacia:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.farmacias = []   

    def agregar(self, farmacia: Farmacia):
        self.farmacias.append(farmacia)

    def mostrarMedicamentosTosSucursal(self, sucursalX):
        for f in self.farmacias:
            if f.sucursal == sucursalX:
                return f.mostrarMedicamentosTos()
        return []

    def buscarFarmaciaConMedicamento(self, nombreMed):
        resultado = []
        for f in self.farmacias:
            if f.buscaMedicamento(nombreMed) is not None:
                resultado.append((f.sucursal, f.direccion))
        return resultado

    def buscarMedicamentosPorTipo(self, tipo):
        lista = []
        for f in self.farmacias:
            lista.extend(f.mostrarMedicamentosX(tipo))
        return lista

    def ordenarPorDireccion(self):
        self.farmacias.sort(key=lambda f: f.direccion.lower())

    def moverMedicamentos(self, tipo, sucA, sucZ):
        fA = None
        fZ = None
        for f in self.farmacias:
            if f.sucursal == sucA:
                fA = f
            if f.sucursal == sucZ:
                fZ = f

        if fA is None or fZ is None:
            return "Sucursal no encontrada."

        mover = [m for m in fA.medicamentos if m.tipo.lower() == tipo.lower()]

        for m in mover:
            fA.medicamentos.remove(m)
            fZ.medicamentos.append(m)

        return f"Movidos {len(mover)} medicamentos de tipo {tipo}."

m1 = Medicamento("Tapsin", 101, "fiebre", 12)
m2 = Medicamento("Jarabe Azul", 102, "tos", 20)
m3 = Medicamento("Mentisan", 103, "tos", 15)

f1 = Farmacia("MiFarma", 1, "Av. América")
f1.agregar(m1)
f1.agregar(m2)

f2 = Farmacia("MiFarma", 2, "Av. Blanco Galindo")
f2.agregar(m3)

arch = ArchFarmacia("farmacias.dat")
arch.agregar(f1)
arch.agregar(f2)

print("\n(a) Medicamentos para la tos:")
for m in arch.mostrarMedicamentosTosSucursal(1):
    print(m)

print("\n(b) Farmacias con Tapsin:")
print(arch.buscarFarmaciaConMedicamento("Tapsin"))

print("\n(c) Medicamentos tipo 'tos':")
for m in arch.buscarMedicamentosPorTipo("tos"):
    print(m)
arch.ordenarPorDireccion()
print("\n(d) Farmacias ordenadas por dirección:")
for f in arch.farmacias:
    print(f)

print("\n(e)", arch.moverMedicamentos("tos", 2, 1))
