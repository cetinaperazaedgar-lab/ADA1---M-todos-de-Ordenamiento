def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista


def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista


# ---------------------- MENÚ PRINCIPAL ----------------------

def main():
    print(40*"=")
    print("Métodos de Ordenamiento")
    print("\n1. Burbuja")
    print("\n2. Inserción")
    print("\n3. Selección")
    print(40*"=")

    opcion = int(input("\nElige una opción: "))
    lista = list(map(int, input("\n Ingresa los números separados por espacio: ").split()))

    if opcion == 1:
        print("\nOrdenando con Burbuja...")
        print(burbuja(lista))
        print(40*"=")


    elif opcion == 2:
        print("\nOrdenando con Inserción...")
        print(insercion(lista))
        print(40*"=")

    elif opcion == 3:
        print("\nOrdenando con Selección...")
        print(seleccion(lista))
        print(40*"=")

    else:
        print("\nOpción inválida")
        print(40*"=")


# Ejecutar programa
main()
