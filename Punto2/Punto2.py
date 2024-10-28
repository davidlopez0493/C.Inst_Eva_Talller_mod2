def eliminar_repetidos(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista


entrada = input("ingrese una lista de números separados por coma: ")


numeros = [int(num.strip()) for num in entrada.split(",")]

resultado = eliminar_repetidos(numeros)
print(f"La lista sin repeticiones es: {resultado}")
