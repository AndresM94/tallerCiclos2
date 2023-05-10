from random import randint

productos_deseados = ["Leche", "Huevos", "Arepas", "Queso", "Plátanos", "Arroz", "Papa", "Pescado"]

tiendas = ["tienda1", "tienda2", "tienda3", "tienda4", "tienda5", "tienda6", "tienda7", "tienda8", "tienda9", "tienda10"]

productos_encontrados = []

productos_comprados = {}

for tienda in tiendas:
    productos_pendientes = []
    productos_comprados[tienda] = 0

    for producto in productos_deseados:
        pregunta = randint(0, 1)

        if pregunta == 1:
            productos_encontrados.append(producto)
            productos_comprados[tienda] += 1
        else:
            productos_pendientes.append(producto)

    productos_deseados = productos_pendientes

    if not productos_deseados:
        break


print("----- Reporte de Compra -----")
print("Productos encontrados:")
for producto in productos_encontrados:
    print(producto)

print("Productos no encontrados:")
for producto in productos_deseados:
    print(producto)


print("----- Reporte de Compras por Tienda -----")
for tienda, cantidad in productos_comprados.items():
    print(f"{tienda}: {cantidad} productos comprados")
