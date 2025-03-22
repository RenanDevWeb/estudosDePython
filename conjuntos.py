lista = set(
    [1,2,3,1,3,4]
)
print(lista)
carros = set(("palio","gol","palio","gol"))
print(carros)


# converta set para list
numeros = {1,2,3,4,5}
numeros = list(numeros)
print(numeros)

#union
conjunto_a =  {1,2}
conjunto_b =  {3,4}
conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)


#intersecção - pega somente o que a de igual entre os conjuntos
conjunto_a =  {1,2,3}
conjunto_b =  {3,4,5}
conjunto_c = conjunto_a.intersection(conjunto_b)
print(conjunto_c)

#diferenca
conjunto_a =  {1,2,3}
conjunto_b =  {3,4,5}
conjunto_c = conjunto_a.difference(conjunto_b)
print(conjunto_c)