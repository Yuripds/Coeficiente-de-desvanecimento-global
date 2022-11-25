
import matplotlib.pyplot as plt
import coeficiente_desvanecimento as cod
import numpy as np

cg_obj = cod.Coeficiente_de_Desvanecimento()



#h=10**(cg_obj.walfishikegami(500, False,2.0*(10**3))/10)


#hc_231 = cg_obj.hatacost231( d=2000,fc=2.0*(10**3))


#desvaneciomento_global =cg_obj.desvanecimentoglobal(d=2000, LOS=False, NN=20, tamanho=10**4, seed=1,fc=2000)
#print(desvaneciomento_global)


#desvaneciomento_global =cg_obj.desvanecimento_modelo3(d=1000, NN=20, tamanho=10**4, seed=1)


tamanho_v = 10**4
d=np.random.uniform(1000,5000,12)
desvaneciomento_global = np.zeros((12,tamanho_v),dtype=complex)
for i in range(12):
    desvaneciomento_global[i,:] = cg_obj.desvanecimento_modelo4(d=d[i], NN=20, tamanho=10**4,seed=i,fc=2000,dmin=1000)



x = range(len(desvaneciomento_global[0]))
plt.plot(x,desvaneciomento_global[0])
plt.yscale("log")
plt.show()