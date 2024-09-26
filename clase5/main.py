from modelos import *

lote1 = TerrenoRectangular(20.5, 11.3)
lote2 = TerrenoRectangular(15.6, 8.9)
lote3 = TerrenoTrapezoidal(10,3.4,2.1)

miUrbanizacion = Urbanizacion("Vista Linda")
miUrbanizacion.agregar_lote(lote1)
miUrbanizacion.agregar_lote(lote2)
miUrbanizacion.agregar_lote(lote3)

areaTotal = miUrbanizacion.area_total()
print(f"El área total de la urbanización es: {areaTotal} m^2")
