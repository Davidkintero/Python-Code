#  def main():
#     print("NÚMERO PRIMO")
#     numero = int(input("Escriba un número entero mayor que 1: "))

#     if numero <= 1:
#         print("¡Le he pedido un número entero mayor que 1!")
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

numeros = [54, 58+5, 45, 12, 57, 84, 64, 25]
i = 0
while (i < len(numeros)):
    if numeros [i] % 2 == 1:
        print(numeros[i])
    i += 1