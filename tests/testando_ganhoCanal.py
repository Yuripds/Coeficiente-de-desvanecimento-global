from coeficienteDevanecimento_GlobalLib import coeficiente_desvanecimento
import numpy as np

def teste_lib():
  qtd_usuarios = 10
  d=np.random.uniform(500,2000,qtd_usuarios)
  dGlobal = np.zeros((qtd_usuarios,10**3),dtype=complex)
  for i in range(qtd_usuarios):
    dGlobal[i,:] = desvanecimentoGlobal(d[i],False,20,10**3,i)

  print (d)
  print(dGlobal)