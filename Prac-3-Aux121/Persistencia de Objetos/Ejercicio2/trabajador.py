class Trabajador:
    def __init__(self, nombre, carnet, salario):
        self.nombre = nombre
        self.carnet = carnet
        self.salario = salario

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "carnet": self.carnet,
            "salario": self.salario
        }

    @staticmethod
    def from_dict(data):
        return Trabajador(
            data["nombre"],
            data["carnet"],
            data["salario"]
        )