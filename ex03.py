numeros = [1, 2, 3, 4, 5, 6, 7]
numeros_multi = []

for cont in range(0, len(numeros)):
    conta = numeros[cont] * numeros[cont]
    numeros_multi.append(conta)
print(f'{numeros_multi}')