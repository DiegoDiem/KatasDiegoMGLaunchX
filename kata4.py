text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth."
"On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
print(' \n')
print('..........Ejercicio 1')
print(' \n')
# Añade el código necesario
# print(text)
#Primero, divide el texto en cada oración para trabajar con su contenido:

texto_dividido=text.split('. ')
# print(texto_dividido)
# Define las palabras pista: average, temperature y distance suenan bien
palabras=['average','temperature','distance']
# print(palabras)

# Ciclo for para recorrer la cadena
for item in texto_dividido:
    for palabra in palabras:
        if palabra in item:
            print(item)
            break
# Ciclo para cambiar C a Celsius
for item in texto_dividido:
    for palabra in palabras:
        if palabra in item:
            print(item.replace(' C', ' Celsius'))
            break

#Ejercicio 2
print(' \n')
print('..........Ejercicio 2')
# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"


# Creamos el título
title= planet+"'s "+name
# Creamos la plantilla
gravity_meters=gravity*1000
plantilla = title + '\n' +"Planet Name: "+name +'\n'+"Gravity: "+str(gravity_meters) + "m/s2"
# Unión de ambas cadenas
print(plantilla)


planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'
title= planet+"'s "+name
# Comprueba la plantilla
print(plantilla)

# Nueva plantilla
nueva_plantilla = title + '\n' +"Planet Name: "+name +'\n'+"Gravity: "+str(gravity_meters) + "m/s2"
print(nueva_plantilla.format(planet=planet,gravity=gravity,name=name))