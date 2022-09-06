lista = []
lista = [1,2,3,4]
x = lista[0]

dicionario = {}
print("Dicionario vazio: ", dicionario)
dicionario = {
    1: 'fabricio',
    2: 'thalita',
    3: 'frederico',
    4: 'telma'
}
print('Dicionario chaves numéricas: ', dicionario)   
print('Chave numérica : 3', dicionario[3])
existe_chave_5 = 5 in dicionario
if existe_chave_5:
    print("Chave 5 ", dicionario[5])
else:
    print("Chave 5 não existe")
