import json
from trabajador import Trabajador

class ArchivoTrabajador:
    def __init__(self, nombreArch):
        self.nombreArch = nombreArch
        self.trabajadores = []
        self.crearArchivo()

    def crearArchivo(self):
        try:
            with open(self.nombreArch, "r") as f:
                data = json.load(f)
                self.trabajadores = [Trabajador.from_dict(d) for d in data]
        except FileNotFoundError:
            self.trabajadores = []
            self.guardarArchivo()

    def guardarArchivo(self):
        with open(self.nombreArch, "w") as f:
            json.dump([t.to_dict() for t in self.trabajadores], f, indent=4)

    def guardarTrabajador(self, t: Trabajador):
        self.trabajadores.append(t)
        self.guardarArchivo()

    def aumentaSalario(self, aumento: float, t: Trabajador):
        for trab in self.trabajadores:
            if trab.carnet == t.carnet:
                trab.salario += aumento
                break
        self.guardarArchivo()

    def buscarMayor(self):
        if not self.trabajadores:
            return None
        return max(self.trabajadores, key=lambda t: t.salario)

    def ordenarSalario(self):
        self.trabajadores.sort(key=lambda t: t.salario)
        self.guardarArchivo()
