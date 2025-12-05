from Charango import Charango
from Charangos import Charangos

manager = Charangos("charangos.json")

c1 = Charango("Madera", 10, [True]*10)
c2 = Charango("Plástico", 8, [True, False, True, False, True, False, False, False, True, True])
c3 = Charango("Metal", 10, [False]*10)

manager.agregar(c1)
manager.agregar(c2)
manager.agregar(c3)

manager.eliminar_malas()

print("Charangos de madera:")
for c in manager.listar_x_material("Madera"):
    print(c.to_dict())

print("\nCharangos con 10 cuerdas:")
for c in manager.buscar_10():
    print(c.to_dict())

manager.ordenar_material()
print("\nCharangos ordenados por material:")
for c in manager.charangos:
    print(c.to_dict())