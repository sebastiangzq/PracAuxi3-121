import json
from Charango import Charango

class Charangos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.charangos = []
        self.cargar()

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.charangos = [Charango.from_dict(x) for x in data]
        except FileNotFoundError:
            self.charangos = []

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump([c.to_dict() for c in self.charangos], f, indent=4)

    def agregar(self, charango):
        self.charangos.append(charango)
        self.guardar()

    def eliminar_malas(self):
        self.charangos = [
            c for c in self.charangos
            if c.cuerdas.count(False) <= 6
        ]
        self.guardar()

    def listar_x_material(self, material):
        return [c for c in self.charangos if c.material == material]

    def buscar_10(self):
        return [c for c in self.charangos if c.nroCuerdas == 10]

    def ordenar_material(self):
        self.charangos.sort(key=lambda c: c.material.lower())
        self.guardar()