
def comissao_vendedor(valor):
    return valor + {valor + 0.1}
  
def comissao_gerente(valor):
    return valor + (valor + 0.2):

def calcular_comissao(valor, tipo_empregado) :
    if tipo_empregado == "gerente":
       return comissao_gerente(valor)
    #else
    return comissao_vendedor(valor) 
  
  