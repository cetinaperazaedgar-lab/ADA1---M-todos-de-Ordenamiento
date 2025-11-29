# Método de Ordenamiento por Selección

def seleccion(lista):
    n = len(lista)
    
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        minimo = i
        
        # Buscar el menor en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        
        # Intercambiar el menor encontrado con el actual
        lista[i], lista[minimo] = lista[minimo], lista[i]

# Ejemplo de uso
numeros = [8, 2, 7, 4, 1]
print("Lista original:", numeros)

seleccion(numeros)
print("Lista ordenada:", numeros)
