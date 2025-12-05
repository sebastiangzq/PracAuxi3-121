import os
import json

class Producto:
    def __init__(self, codigo: int, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}"


class ArchivoProducto:
    def __init__(self, nombre_archivo: str):
        self.nomA = nombre_archivo

    def crearArchivo(self):
        """Crea el archivo si no existe."""
        if not os.path.exists(self.nomA):
            with open(self.nomA, "w") as f:
                json.dump([], f)

    def guardarProducto(self, p: Producto):
        """Guarda un objeto Producto en el archivo."""
        self.crearArchivo()
        with open(self.nomA, "r") as f:
            lista = json.load(f)

        lista.append({
            "codigo": p.codigo,
            "nombre": p.nombre,
            "precio": p.precio
        })

        with open(self.nomA, "w") as f:
            json.dump(lista, f, indent=4)

    def buscaProducto(self, c: int):
        """Devuelve un Producto buscado por código."""
        self.crearArchivo()
        with open(self.nomA, "r") as f:
            lista = json.load(f)

        for item in lista:
            if item["codigo"] == c:
                return Producto(item["codigo"], item["nombre"], item["precio"])
        return None

    def calcularPromedio(self):
        """Devuelve el promedio de precios."""
        self.crearArchivo()
        with open(self.nomA, "r") as f:
            lista = json.load(f)

        if not lista:
            return 0

        total = sum(item["precio"] for item in lista)
        return total / len(lista)

    def productoMasCaro(self):
        """Retorna el producto con mayor precio."""
        self.crearArchivo()
        with open(self.nomA, "r") as f:
            lista = json.load(f)

        if not lista:
            return None

        max_item = max(lista, key=lambda x: x["precio"])
        return Producto(max_item["codigo"], max_item["nombre"], max_item["precio"])
arch = ArchivoProducto("productos.json")

# Agregar productos
arch.guardarProducto(Producto(1, "Mouse", 10.5))
arch.guardarProducto(Producto(2, "Teclado", 25.0))
arch.guardarProducto(Producto(3, "Monitor", 150.0))

# Buscar producto
p = arch.buscaProducto(2)
if p:
    print("Producto encontrado:", p)
else:
    print("Producto no encontrado.")

# Promedio de precios
print("Promedio de precios:", arch.calcularPromedio())

# Producto más caro
mas_caro = arch.productoMasCaro()
print("Producto más caro:", mas_caro)
