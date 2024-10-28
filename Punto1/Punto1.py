def suma_numeros_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

entrada = input("ingrese una lista de números separados por coma: ")

numeros = [int(num.strip()) for num in entrada.split(",")]

resultado = suma_numeros_pares(numeros)
print(f"La suma de los números pares es: {resultado}")
