def burbuja(lista):
    n = len(lista)
    print("Lista original:", lista)

    for i in range(n - 1):
        print(f"\n--- Pasada {i + 1} ---")
        for j in range(n - 1 - i):
            print(f"Comparando {lista[j]} y {lista[j+1]}")

            if lista[j] > lista[j + 1]:
                print(f"  -> Se intercambian {lista[j]} y {lista[j+1]}")
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                print("  -> No se intercambian")

            print("  Estado actual:", lista)

    print("\nLista ordenada:", lista)


# Ejemplo de uso
numeros = [5, 2, 9, 1, 3]
burbuja(numeros)
