# Somar todos os elementos da lista
# com laço de repetição

lista = [1,2,3,4,5,6,7,8,9,10]

# blocos de instrução: identação

for valor in lista:
# Início do bloco de instruções

    soma = 0
    if valor % 2 == 0:
      soma = soma + valor
 
    soma = soma + valor
    print("Resultado:", soma)
    
    soma = sum(lista)
    print('Resultado: ', soma)

# Fim do for     
    soma = 0
      
    for valor in lista:
        
        #Filtro
        if valor % 2 == 1:
           continue
      
           soma = soma + valor
    
    print("Resultado: ", soma)