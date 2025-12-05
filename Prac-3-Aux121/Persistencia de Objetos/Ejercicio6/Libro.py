class Libro:
    def __init__(self, codLibro, titulo, precio):
        self.codLibro = codLibro
        self.titulo = titulo
        self.precio = precio


class Cliente:
    def __init__(self, codCliente, nombre, apellido):
        self.codCliente = codCliente
        self.nombre = nombre
        self.apellido = apellido


class Prestamo:
    def __init__(self, codLibro, codCliente, cantidad):
        self.codLibro = codLibro
        self.codCliente = codCliente
        self.cantidad = cantidad


class ArchLibro:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)


class ArchCliente:
    def __init__(self):
        self.clientes = []

    def agregar(self, cliente):
        self.clientes.append(cliente)


class ArchPrestamo:
    def __init__(self):
        self.prestamos = []

    def agregar(self, prestamo):
        self.prestamos.append(prestamo)


def libros_entre_precios(archLibros, x, y):
    return [l for l in archLibros.libros if x <= l.precio <= y]


def ingreso_por_libro(archPrestamos, archLibros, codLibro):
    libro = next((l for l in archLibros.libros if l.codLibro == codLibro), None)
    if not libro:
        return 0
    total_cant = sum(p.cantidad for p in archPrestamos.prestamos if p.codLibro == codLibro)
    return total_cant * libro.precio


def libros_nunca_prestados(archLibros, archPrestamos):
    prestados = {p.codLibro for p in archPrestamos.prestamos}
    return [l for l in archLibros.libros if l.codLibro not in prestados]


def clientes_de_libro(archClientes, archPrestamos, codLibro):
    clientes_ids = {p.codCliente for p in archPrestamos.prestamos if p.codLibro == codLibro}
    return [c for c in archClientes.clientes if c.codCliente in clientes_ids]


def libro_mas_prestado(archPrestamos, archLibros):
    if not archPrestamos.prestamos:
        return None

    conteo = {}
    for p in archPrestamos.prestamos:
        conteo[p.codLibro] = conteo.get(p.codLibro, 0) + p.cantidad

    cod_max = max(conteo, key=conteo.get)
    return next(l for l in archLibros.libros if l.codLibro == cod_max)


def cliente_con_mas_prestamos(archPrestamos, archClientes):
    if not archPrestamos.prestamos:
        return None

    conteo = {}
    for p in archPrestamos.prestamos:
        conteo[p.codCliente] = conteo.get(p.codCliente, 0) + p.cantidad

    cod_max = max(conteo, key=conteo.get)
    return next(c for c in archClientes.clientes if c.codCliente == cod_max)


if __name__ == "__main__":
    libros = ArchLibro()
    clientes = ArchCliente()
    prestamos = ArchPrestamo()

    libros.agregar(Libro(1, "Libro A", 100))
    libros.agregar(Libro(2, "Libro B", 200))
    libros.agregar(Libro(3, "Libro C", 300))

    clientes.agregar(Cliente(1, "Juan", "Pérez"))
    clientes.agregar(Cliente(2, "Ana", "Gómez"))

    prestamos.agregar(Prestamo(1, 1, 2)) 
    prestamos.agregar(Prestamo(2, 2, 1)) 
    prestamos.agregar(Prestamo(1, 2, 1)) 
    print("a) Libros entre 100 y 250:")
    for l in libros_entre_precios(libros, 100, 250):
        print(l.titulo)

    print("\nb) Ingreso por Libro A:", ingreso_por_libro(prestamos, libros, 1))

    print("\nc) Libros nunca prestados:")
    for l in libros_nunca_prestados(libros, prestamos):
        print(l.titulo)

    print("\nd) Clientes que llevaron Libro A:")
    for c in clientes_de_libro(clientes, prestamos, 1):
        print(c.nombre)

    print("\ne) Libro más prestado:", libro_mas_prestado(prestamos, libros).titulo)

    print("\nf) Cliente con más préstamos:", cliente_con_mas_prestamos(prestamos, clientes).nombre)