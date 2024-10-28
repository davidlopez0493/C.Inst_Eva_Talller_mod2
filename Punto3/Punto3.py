def invertir_lista(lista):
    return lista[::-1]


entrada = input("ingrese una lista de números separados por coma: ")

lista_original = [elemento.strip() for elemento in entrada.split(",")]

resultado = invertir_lista(lista_original)
print(f"La lista invertida es: {resultado}")
