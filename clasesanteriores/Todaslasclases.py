# n = int(input("Enter the number: "))                      
# p = len(str(n))                                           
# s = 0                                                     
# k = n                                                     
# while k>0:                                                
#     d = k%10                                              
#     s = s + (d**p)                                        
#     k = k//10                                             
# if n == s:                                                
#     print('{} is an Armstrong number'.format(n))          
# else:                                                       
#     print('{} is not an Armstrong number'.format(n)) 

# try:
#     y = input('Ingrese un numero: ')    #ingresa un numero
#     x = int(y)                          # lo convierte en entero
#     c = len(str(x))                     #identifica la cantidad de cifras de la cadena y lo guarda
#     p = 0                               #borra variable para elevar portencia
#     r = x                               #guarda el valor del numero ingresado en un registro
#     while r > 0:
#         d = r%10                        #saca el modulo para sacar digitos
#         p = p = (d**c)                  #eleva la potencia
#         r = r//10                       #saca la division entera
#     if x == p:                          #compara el resultado de la suma de las potencia con el numero
#         print(x, 'es un numero armstrong')
#     else:
#         print(x, 'no es un numero armstrong')
# except:
#     print('por favor ingresar solo numeros')

# n = 5
# valor_absoluto = n if n > 0 else n * -1
# print(valor_absoluto)
# print(True or 'valor')

# 56 quiero expresar que el numero 56 como un numero binario, (56 dividido en 2 = 28 y 28 se devidee entre 2 = 14 y queda sobrando 0 y 14 se divide entre 2 da 7 sobrando 0, 7 divido da 3 queda sobrando 1, 3 se divide entre 3 resultado 1 queda sobrando 1, el numero binario seria 111000)
# 56 el numero binario es 111000

# numero = int(input('Introduce el número a convertir a binario: '))

# def procedimiento(decimal):
#     binario = ''
#     while decimal // 2 != 0:
#         binario = str(decimal % 2) + binario
#         decimal = decimal // 2
#     return str(decimal) + binario


# print(procedimiento(numero))

# numero = int(input('Ingrese un numero: '))
# binaro = ''
# x = numero
# while x >=1:
#     r = x % 2
#     x = x // 2
#     binaro = binaro + str(r)

# print(binaro[::-1])

# lista = [True, '123',8,3.9]
# for i in lista:
#     print(i)

# lista = [True, '123',8,3.9]
# for i in range (0,len(lista)):
# #     print(lista[i])

# lista = [1,30,80,65]
# menor = None
# mayor = None
# for numero in lista:
#     if menor == None and mayor == None:
#         menor = numero
#         mayor = numero
#     else:
#         if numero < menor:
#             menor = numero
#         if numero > mayor:
#             mayor = numero

# print(f'El numero mayor es: {mayor}')
# print(f'El numero menor es {menor}')

# print(f'El numero mayor de la lista es {max(lista)}')
# print(f'El numero menor de la lista es {min(lista)}')


# #fibbonaci
# n = 7
# a,b = 0,1
# fib = str(a)+str(b)
# # 0 1 1 2 3 5 8
# # for i in range (n -2):
# #     b = b + a 
# #     a = b 
# #     fib = fib+str(a)+str(b)
# # print(fib)

# while a < n:
#     print(a,end='')
#     a,b = b,a+b
# print()

# nombre = input('ingrese el nombre a buscar')
# lista_nombres = ('maria','juan','saul','pedro','martha')
# sw = False
# if nombre in lista_nombres:
#     sw = True
# if sw:
#     print('Nombre encontrado')
# else:
#     print('nombre no encontrado')

# for i in range (1,10):
#     for j in range (1,5):
#          print(f'El valor de i {i} y el valor de j {j}' )

# #generar los primeros 10 numeros primos




# numero_primos = int(input('Ingrese numeros a encontrar....'))
# numero = 2
# cont = 0
# while cont < numero_primos:
#     counter = 0
#     for i in range (1,numero+1):
#         if numero % i == 0:
#             counter +=1
#     if counter == 2:
#         cont += 1
#         print(f'Numero primo {numero}')
#     numero = numero + 1

# op = 0
# salir = True
# while salir:
#     print('1: crear cliente')
#     print('2: buscar un cliente')
#     print('3: actualizar cliente')
#     print('4: salir')
#     op = int(input('ingrese un valor enntre 1 y 4: '))
#     if op == 1:
#         print('opcion 1')
#     elif op == 2:
#         print ('option 2')
#     elif op == 3:
#         print ('option 3')
#     elif op == 4:
#         print('option 4')
#         salir = False
#     else:
#         print('opcion invalida, por favor valor entre 1 y 4')


# numero1 = int(input("Introduce tu primer número: ") )
# numero2 = int(input("Introduce tu segundo número: ") )

# opcion = 0
# while True:
#     print("""
#     Calculadora pythontic2020, que deseas:
    
#     1) Sumar 
#     2) Restar
#     3) Multiplicar 
#     4) Cambiar los números 
#     5) Apagar
#     """)
#     # opcion = int(input("Elige una opción: ") )     

    # if opcion == 1:
    #     print(" ")
    #     print("resultado: La suma de",numero1,"+",numero2,"es igual a",numero1+numero2)
    # elif opcion == 2:
    #     print(" ")
    #     print("resultado: La resta de",numero1,"-",numero2,"es igual a",numero1-numero2)
    # elif opcion == 3:
    #     print(" ")
    #     print("resultado: El producto de",numero1,"*",numero2,"es igual a",numero1*numero2)
    # elif opcion == 4:
    #     numero1 = int(input("Introduce tu primer número: ") )
    #     numero2 = int(input("Introduce tu segundo número: ") )
    # elif opcion == 5:
    #     break
    # else:
    #     print("Opción incorrecta")

# import time
# password = 'miclave'
# salir = True
# cont = 0
# while salir:
#     clave = input('Ingrese Clave: ')
#     if clave != password:
#         cont += 1
#     else:
#         print('Ingreso Exitoso')
#         salir = False
#     if cont == 4:
#         print('Ha errado 4 veces y debe esperar 5 segundos ')
#         time.sleep(5)
#         cont = 0
# # print('Fin del programa!!')
# palabra = input('Ingrese una palabra')
# invertida = ''
# original_sin_espacio = ''
# for i in range(len(palabra)-1,-1,-1):
#     letra = palabra[i]
#     if letra != ' ':
#         invertida = invertida + letra
# if palabra == invertida:
#     print('Es palindromo')
# else:
#     print('No es palindromo')


#hacer una funcion que me determine si un numero es par o impar
# def main():
#     numero = int(input("Escriba un número entero mayor que 1: "))

#     if numero <= 1:
#         print("¡he dicho numero mayor a 1!")
#     else:
#         contador = 0
#         for i in range(1, numero + 1):
#             if numero % i == 0:
#                 contador = contador + 1
#         if contador == 2:
#             print(f"{numero} es primo.")
#         else:
#             print(f"{numero} no es primo.")


# if __name__ == "__main__":
#     main()


# a = int(input('por favor ingrese un numero: '))

# if a % 2 == 0:
#     print(f"El valor del valor de {a} es numero par")
# else:
#     a % 2 != 0
#     print(f"El valor de a {a} es numero impar")
# def espar(num):
#     bl = False
#     if num % 2 == 0:
#         bl = True
#     return bl 
# print()
# espar(9)

# def espar():
#     numero = int(input("Escriba un número entero para saber si es impar\par: "))
#     if numero % 2 == 0:
#                 print(f'{numero} es par')
#     else:
#         print(f"{numero} no es par.")
       
# if __name__ == "__main__":
#      espar()

# def espar(num):
#     bl = False
#     if num % 2 == 0:
#         bl = True
#     return bl 

# cont = 1
# verd = 0
# while verd <= 15:
#     bll2 = espar(cont)
#     if bll2:
#         print(cont)
#         verd += 1
#     cont += 1
    
# lista = [4,4,4,4,8]

# def mayores_promedio(lista) -> list:
#     promedio = 0
#     suma = 0
#     mayores = []
#     contador = 0
#     for numero in lista:
#         suma += numero
#         contador += 1
#     promedio = suma/contador
#     print(promedio)
#     for numero in lista:
#         if numero>promedio:
#             mayores.append(numero)

#     return mayores

# prueba = mayores_promedio(lista)
# for i in prueba:
#     print(i)

# listado = [4.5,6.7,8.12,15]
# def sumatoria (lista):
#     suma = 0
#     for i in lista:
#         suma += 1
#     return suma

# def promedio (lista):
#     p= sumatoria(lista)/len(lista)
#     return p

# def mayorquepromedio(lista):
#     valores = []
#     prom = promedio(lista)
#     print (prom)
#     for valor in lista:
#         if valor >prom:
#             valores.append(valor)
#     return valores

# print(mayorquepromedio(listado))
        
# # import random
# # print(int(random.random()*100))

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")

# poblacion = 100
# mujeres = 70
# hombres = 40

# resultado1 = hombres + mujeres == poblacion
# print(resultado1)

# opcion = input('Escribe la opcion: ')

# if opcion == '1':
#     print('Escogio la opcion 1')
# elif opcion == '2':
#     print('Escogio la opcion 2')
# elif opcion == '3':
#     print('Escogio la opcion 3')
# elif opcion == '4':
#     print('Escogio la opcion 4')
# elif opcion == '5':
#     print('Escogio la opcion 5')
# else:
#     print('Opcion invalida')



# numero1 = int(input('Ingrese un numero: '))

# if numero1 % 2 == 0:
#     print(f'{numero1} es un numero par ')
# else:
#     print(f'{numero1} es un numero impar ')

# recibir valor 
# y evaluar

# si ese valor esta dentro de un rango o categoria

# si esta entre 10 y 14 es categoria infantil
# si esta entre 15 y 17 es categoria juvenil
# si esta entre 18 y 20 es sub20
# si es mayor a los 20 es profesional

# edad = int(input('Escribe tu edad entre los 10 y 45 años para determinar tu categoria: '))

# if edad >= 10 and edad <= 14:
#     print('Categoria infantil')
# elif edad >= 15 and edad <= 17:
#     print('Categoria juvenil')
# elif edad >= 18 and edad <=20:
#     print('Categoria sub20 ')
# elif edad > 20 and edad <= 45:
#     print('Categoria profesional')

# else:
#     print('Ingrese un valor correcto')
# edad = 58
# genero = 'F'
# semanas = 240

# if genero == 'F':
#     if edad >= 58:
#         if semanas >= 250:
#             print('Se puede pensionar')
#         else:
#             print('Le faltan '+str( 250 - semanas ) +' semanas')
#     else:    
#         print('Le faltan '+str( 58 - edad ) +' años')
# elif genero == 'M':
#     if edad >= 60:
#         if semanas >= 255:
#             print('Se puede pensionar')
#         else:
#             print('Le faltan '+str( 255 - semanas ) +' semanas')
#     else:    
#         print('Le faltan '+str( 60 - edad ) +' años')

# autos = {'autos':{
#         1:{'marca':'Tesla',
#            'modelos':{
#                1:'Model S',
#                2:'Model E',
#                3:'Model X',
#                4:'Model Y',
#                }
#            },
#         2:{'marca':'Toyota',
#            'modelos':{
#                1:'Fortuner',
#                2:'Prado',
#                3:'Tundra',
#                4:'Corola',
#                }
#            },
#         3:{'marca':'Range Rover',
#            'modelos':{
#                1:'Evoque',
#                2:'Defender',
#                }
#            },
#         4:{'marca':'Mazda',
#            'modelos':{
#                1:'Mazda 3',
#                2:'Mazda 2',
#                3:'CX 30',
#                }
#            },
#         5:{'marca':'Audi',
#            'modelos':{
#                1:'A7',
#                2:'A5',
#                3:'A3',
#                }
#            }
#         }
#         }
# m1 = len(autos['autos'][1]['modelos'])
# m2 = len(autos['autos'][2]['modelos'])
# m3 = len(autos['autos'][3]['modelos'])
# m4 = len(autos['autos'][4]['modelos'])
# m5 = len(autos['autos'][5]['modelos'])


# print(m1, m2, m3, m4, m5)

# palabra = 'Un texto de varias palabras'

# # print(palabra[0])
# # print(palabra[1])
# print(palabra.replace('a' , 'o'))

# numeros = [54, 58, 45, 12]
# print(numeros[-1])

# promedio mas alto dentro de los elementos

numeros1 = [59, 58+5, 45-5, 12*2]
numeros2 = [54, 58+5, 45, 12+24]
numeros3 = [54+2, 58+5, 45, 12]
numeros4 = [4, 58+5, 45*2, 12]
def max_avg_num(n1, n2, n3, n4):
    avg_1 = sum(n1)/len(n1)
    avg_2 = sum(n2)/len(n2)
    avg_3 = sum(n3)/len(n3)
    avg_4 = sum(n4)/len(n4)
    return max(avg_1, avg_2, avg_3, avg_4)
print(max_avg_num(numeros1,numeros2,numeros3,numeros4))

# print(sum(numeros1)/len(numeros1))
# print(sum(numeros2)/len(numeros2))
# print(sum(numeros3)/len(numeros3))
# print(sum(numeros4)/len(numeros4))