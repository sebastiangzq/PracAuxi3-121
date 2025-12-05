from datetime import datetime

class Alimento:
    def __init__(self, nombre, fechaVencimiento, cantidad):
        self.nombre = nombre
        self.fechaVencimiento = fechaVencimiento 
        self.cantidad = cantidad

    def fecha_datetime(self):
        return datetime.strptime(self.fechaVencimiento, "%d/%m/%Y")


class ArchRefrí:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alimentos = []  

    def crear(self, alimento):
        self.alimentos.append(alimento)

    def modificar_por_nombre(self, nombre, nuevaFecha=None, nuevaCantidad=None):
        for a in self.alimentos:
            if a.nombre == nombre:
                if nuevaFecha is not None:
                    a.fechaVencimiento = nuevaFecha
                if nuevaCantidad is not None:
                    a.cantidad = nuevaCantidad
                return True
        return False

    def eliminar_por_nombre(self, nombre):
        for a in self.alimentos:
            if a.nombre == nombre:
                self.alimentos.remove(a)
                return True
        return False

    def alimentos_caducados_antes(self, fechaX):
        x = datetime.strptime(fechaX, "%d/%m/%Y")
        return [a for a in self.alimentos if a.fecha_datetime() < x]

    def eliminar_sin_stock(self):
        self.alimentos = [a for a in self.alimentos if a.cantidad > 0]

    def alimentos_vencidos(self):
        hoy = datetime.today()
        return [a for a in self.alimentos if a.fecha_datetime() < hoy]

    def alimento_max_cantidad(self):
        if not self.alimentos:
            return None
        return max(self.alimentos, key=lambda a: a.cantidad)


if __name__ == "__main__":
    refri = ArchRefrí("MiRefrigerador")

    refri.crear(Alimento("Leche", "10/05/2024", 2))
    refri.crear(Alimento("Yogurt", "01/04/2024", 5))
    refri.crear(Alimento("Queso", "20/04/2024", 0))
    refri.crear(Alimento("Jamón", "15/06/2024", 3))

    print("\nb) Caducados antes de 15/05/2024:")
    for a in refri.alimentos_caducados_antes("15/05/2024"):
        print(a.nombre)

    refri.eliminar_sin_stock()

    print("\nd) Alimentos vencidos:")
    for a in refri.alimentos_vencidos():
        print(a.nombre)

    maximo = refri.alimento_max_cantidad()
    print("\ne) Alimento con más cantidad:", maximo.nombre if maximo else "Ninguno")
