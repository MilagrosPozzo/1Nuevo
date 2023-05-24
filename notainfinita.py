# Defino las variables promedio, suma, contador de notas totales y contador de insficientes.
suma = 0
promedio = 0.0
cont_insuf = 0
cont_notas = 0
while (True): #si no se pone el True con T mayúscula, no lo toma.
 num = int(input("ingrese la calificacion: "))
 if num <6: 
  cont_insuf += 1
  #si es menor a 6 el contador de insuficientes corre.
 if num > 12 or num < 1:
  break  #si el numero es menor a 12 o mayor a 1 se corta el while.
 suma = suma + num # suma += num
 cont_notas += 1

if cont_notas != 0:
 promedio = suma / cont_notas
  #si contador de notas no es igual a cero procede a dividir la suma del total de notas x la cantidad de notas ingresadas.
else:
 promedio = 0

 
#Respondo el promedio de notas
print("Promedio de notas es:", promedio)
print("usted ingreso", cont_notas , "notas")
print("de las cuales", cont_insuf, "son insuficientes")

#agregar al codigo dos preguntas q aumenten una variable sola cant_insuficiente.