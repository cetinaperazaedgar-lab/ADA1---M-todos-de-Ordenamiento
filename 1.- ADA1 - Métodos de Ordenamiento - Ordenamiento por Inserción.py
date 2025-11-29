# Método de Ordenamiento por Inserción

def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        
        # Mover los elementos mayores una posición adelante
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = actual

# Ejemplo de uso
numeros = [9, 3, 1, 5, 4]
print("Lista original:", numeros)

insercion(numeros)
print("Lista ordenada:", numeros)
