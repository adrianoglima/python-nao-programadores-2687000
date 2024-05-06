# Crie uma lista apenas com elementos numéricos
numeros = [1,2,3,4,5,6]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
misto = [1,"adriano",[2,"lima","dada"], "julia"]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(numeros[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(numeros[1:-1:2])
# Remova da lista o último item
misto.pop()
# Insira na lista um novo item
misto.append('python')
# Remova da lista um item específico
numeros.remove(3)
print('--------------')
print(numeros)
print(misto)