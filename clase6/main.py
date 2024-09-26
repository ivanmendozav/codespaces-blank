from modelos import *

# Dueño
yo = Persona("0103422473","Ivan Mendoza",44)

# Coleccion de autos de Ivan
cadilac = Auto("ABL4533","Cadilac",12000)
mercedez = Auto("ABI3325","Mercedes-Benz",8000)

# Registrar autos
yo.registrar_auto(mercedez)
yo.registrar_auto(cadilac)

# Calcular el impuesto total
total = yo.calc_impuestos()
print(f"{yo.nombre} debe pagar de impuestos ${total}.")

# Dueño 2
tu = Persona("0103422474","Pablo Mendoza",54)

# Coleccion de autos de Pablo
auto1 = Auto("ABL4531","Cadilac",12000)
auto2 = Auto("ABI3025","Mercedes-Benz",8000)

# Registrar autos
tu.registrar_auto(auto1)
tu.registrar_auto(auto2)

# Canton que incluye a todas las personas
canton = Canton("Gualaceo")
canton.registrar_habitante(yo)
canton.registrar_habitante(tu)

# Calcular el impuesto total
total = canton.calcular_impuestos()
print(f"En el canton {canton.nombre} se recaudaron ${total} en impuestos.")

