import json
import os
class Estudiante:
    def __init__(self, ru, nombre, paterno, materno, edad):
        self.ru = ru
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad

    def __str__(self):
        return f"{self.ru} - {self.nombre} {self.paterno} {self.materno}, {self.edad} años"


class Nota:
    def __init__(self, materia, notaFinal, estudiante: Estudiante):
        self.materia = materia
        self.notaFinal = notaFinal
        self.estudiante = estudiante

    def to_dict(self):
        return {
            "materia": self.materia,
            "notaFinal": self.notaFinal,
            "estudiante": {
                "ru": self.estudiante.ru,
                "nombre": self.estudiante.nombre,
                "paterno": self.estudiante.paterno,
                "materno": self.estudiante.materno,
                "edad": self.estudiante.edad,
            }
        }

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.materia}: {self.notaFinal}"


class ArchiNota:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def crearArchivo(self):
        if not os.path.exists(self.nombreArchivo):
            with open(self.nombreArchivo, "w") as f:
                json.dump([], f)

    def agregarNotas(self, listaNotas):
        self.crearArchivo()
        with open(self.nombreArchivo, "r") as f:
            data = json.load(f)

        for nota in listaNotas:
            data.append(nota.to_dict())

        with open(self.nombreArchivo, "w") as f:
            json.dump(data, f, indent=4)

    def promedioNotas(self):
        self.crearArchivo()
        with open(self.nombreArchivo, "r") as f:
            data = json.load(f)

        if not data:
            return 0

        total = sum(item["notaFinal"] for item in data)
        return total / len(data)

    def mejoresNotas(self):
        self.crearArchivo()
        with open(self.nombreArchivo, "r") as f:
            data = json.load(f)

        if not data:
            return []

        max_nota = max(item["notaFinal"] for item in data)

        mejores = []
        for item in data:
            if item["notaFinal"] == max_nota:
                e = item["estudiante"]
                estudiante = Estudiante(e["ru"], e["nombre"], e["paterno"], e["materno"], e["edad"])
                mejores.append(Nota(item["materia"], item["notaFinal"], estudiante))

        return mejores

    def eliminarMateria(self, materia):
        self.crearArchivo()
        with open(self.nombreArchivo, "r") as f:
            data = json.load(f)

        nueva_lista = [item for item in data if item["materia"] != materia]

        with open(self.nombreArchivo, "w") as f:
            json.dump(nueva_lista, f, indent=4)
        return len(data) - len(nueva_lista)  

e1 = Estudiante(1, "Luis", "Perez", "Lopez", 20)
e2 = Estudiante(2, "Ana", "Gomez", "Rios", 22)
e3 = Estudiante(3, "Marta", "Soto", "Lima", 21)

n1 = Nota("Matemática", 85, e1)
n2 = Nota("Matemática", 95, e2)
n3 = Nota("Física", 95, e3)
n4 = Nota("Química", 70, e1)

archivo = ArchiNota("notas.json")

archivo.agregarNotas([n1, n2, n3, n4])

print("Promedio:", archivo.promedioNotas())

print("\nEstudiantes con la mejor nota:")
for nota in archivo.mejoresNotas():
    print(nota)

eliminados = archivo.eliminarMateria("Química")
print(f"\nRegistros eliminados de Química: {eliminados}")
