## El programa se ejecuta desde la terminal con el mensaje siguiente: python3 program.py

# program.py
print('--------Parte 1: Un programa en Python')
sum = 1 + 2
print(sum)


print('--------Parte 2: Función print()')
print('Hola desde la consola')

print('--------Parte 3: Variables')
sum = 1 + 2 # 3
product = sum * 2
print(product)


print('--------Parte 4: Tipos de datos')
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# Declaramos la variable
distancia_a_alfa_centauri = 4.367 # Parece un decimal flotante
# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)
print(type(distancia_a_alfa_centauri))

print('--------Parte 5: Operadores')
left_side = 10
right_side = 5
print(left_side / right_side )# 2

print('--------Parte 6: Fechas')
# Importamos la biblioteca 
from datetime import date
# Obtenemos la fecha de hoy
date=date.today()
# Mostramos la fecha en la consola
print(date)

print('--------Parte 7: Conversión de tipos de datos')
#Fecha + mensaje
#!print("Today's date is: " + date.today())
print("Today's date is: " + str(date.today()))
print("Today's date is: " + str(date))


print('--------Parte 8:Recopilar información')
#Capturar información con input()
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)
#Resultado: Saludos: Diego

print('--------Parte 9: Trabajar con números')
#Captura información con números
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)
#Imprime un número seguido del otro

print('--------Parte 10: Trabajar con números sin cadena de texto')
print(int(first_number) + int(second_number))
#Imprime la suma del primer número y del segundo número