
import matplotlib.pyplot as plt


import coeficiente_desvanecimento as cod


cg_obj = cod.Coeficiente_de_Desvanecimento()



h=10**(cg_obj.walfishIkegami(500, False,2.0*(10**9))/10)


hc_231 = cg_obj.hataCost231( d=2000,fc=2.0*(10**9))


desvaneciomento_global =cg_obj.desvanecimentoGlobal(d=500, LOS=False, NN=20, tamanho=10**4, seed=1,fc=2.0*(10**3))
#print(desvaneciomento_global)

y = abs(desvaneciomento_global[0])


x = range(len(desvaneciomento_global[0]))
plt.plot(x,abs(desvaneciomento_global[0]))
plt.yscale("log")
plt.show()