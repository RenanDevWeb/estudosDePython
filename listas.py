carros = ["toyota","corola","gol"]

for carro in carros:
    print(carro)

for indice,carro in enumerate(carros):
    print(f"{indice+1}: {carro}")

# //coompreensao de lista

numeros = [1,5,76,7,8,341,12,3,5,6]
# pares =[]

# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)

parescoompreension = [numero for numero in numeros if numero % 2 == 0]
print(parescoompreension)

numerosAoQuadrado = [numeroquadrado ** 2 for numeroquadrado in numeros ]
print(numerosAoQuadrado)

# metodos de lista 
lista = []
lista.append(1)
lista.append("test")
lista.append([40,20,30])
print(lista)
lista.clear()
print(lista)
lista.copy()
# .extend junta as listas
# .index() mostra o index da lista 
# .pop() retira o ultimo elemento