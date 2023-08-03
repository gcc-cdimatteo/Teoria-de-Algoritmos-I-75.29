def menor_numero(L):
    n = len(L)
    print(f'la lista es: {L}')

    if n == 1: return 0
    
    if L[0]+1 != L[1]: 
        print("SALTO")
        return L[0]+1
    elif n == 2: return 0

    izq = L[0:int(n/2)]
    der = L[int(n/2):n]
    print(f'IZQ {izq}')
    print(f'DER {der}')

    menor_izq = menor_numero(izq)
    if menor_izq != 0: return menor_izq

    if izq[-1]+1 != der[0]: return izq[-1]+1

    return menor_numero(der)

# arr = [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]
# arr = [1, 2, 3, 5, 8, 9, 11, 12, 13, 14, 20, 22]
# arr = [1, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 20, 22]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22]

print(menor_numero(arr))