from trabajador import Trabajador
from archivo_trabajador import ArchivoTrabajador

arch = ArchivoTrabajador("trabajadores.json")

t1 = Trabajador("Ana", 123, 3000)
t2 = Trabajador("Luis", 456, 4500)
t3 = Trabajador("Marta", 789, 2800)

arch.guardarTrabajador(t1)
arch.guardarTrabajador(t2)
arch.guardarTrabajador(t3)

arch.aumentaSalario(500, t1)

mayor = arch.buscarMayor()
print("Trabajador con mayor salario:")
print(mayor.to_dict())

arch.ordenarSalario()
print("\nTrabajadores ordenados por salario:")
for t in arch.trabajadores:
    print(t.to_dict())
