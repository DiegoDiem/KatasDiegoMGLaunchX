from site import venv
# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

#Problema 1
print("----Problema 1")
velocidad_asteroide = 49

if velocidad_asteroide > 25:
    print("!ADVERTENCIA! Se acerca un asteroide a alta velocidad: "+ str(velocidad_asteroide)+"km/s")
else:
    print("Velocidad moderada del asteroide")


#Problema 2
print("----Problema 2")

velocidad_asteroide2 = 19

if velocidad_asteroide2>=20:
    print("Busquen buscar un asteroide en el cielo, posiblemente produce un rayo de luz")
else:
    print("No hay asteroides cerca")


#Problema 3
print("----Problema 3")
dimension_asteroide = 1
velocidad_asteroide3=1

if dimension_asteroide>25 and dimension_asteroide<1000 and velocidad_asteroide3>25:
    print("!ADVERTENCIA, el impacto causara mucho daño!")
elif velocidad_asteroide3>=20:
    print("Hay un rayo en el cielo de luz")
elif dimension_asteroide<25:
    print("No pasa nada")

