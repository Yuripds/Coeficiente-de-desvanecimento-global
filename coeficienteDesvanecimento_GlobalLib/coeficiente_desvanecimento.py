import numpy as np
import math
import random
from coeficienteDevanecimento_GlobalLib import fading_doppler


class Coeficiente_de_Desvanecimento:

    def fading(self, tamanho, seed):
        h = np.zeros((1, tamanho), dtype=complex)
        conc = 1.0
        an, doppler = fading_doppler.Fading_Doppler.gcanal(self.NN, seed)
        for j in range(tamanho):
            h[:, j] = fading_doppler.Fading_Doppler.gera_canal(self.NN, conc, an, doppler)
            conc = conc+1.0
        return h

    # d é dado em metros
    def hataCost231(self, d):
        fc = 1.9*(10**6)
        ht = 15
        hr = 1.65
        d0 = 10
        d1 = 50
        L = 46.3 + (33.9*(math.log(fc, 10))) - (13.82*(math.log(ht, 10))) - 0.8 - \
            (((1.11*(math.log(ht, 10))) - 0.7))*hr + (1.56*(math.log(fc, 10)))

        PL = -L

        if (d > d0) & (d <= d1):
            PL = PL - (15*math.log(d1, 10)) - (20*math.log(d, 10))
        elif d > d1:
            PL = PL - (35*math.log(d, 10))
        else:
            PL = PL - (15*math.log(d1, 10)) - (20*math.log(d0, 10))

        return PL

    # d é dado em mestros
    def walfishIkegami(self, d, LOS):
        fc = 1.9*(10**6)
        if LOS == True:
            PL = 35.4-(26*math.log(d, 10)) - (20*math.log(fc, 10))
        else:
            PL = 55.9 - (38*math.log(d, 10)) - \
                ((24.5 + ((1.5*fc)/925))*math.log(fc, 10))

        return PL

    def desvanecimentoGlobal(self, d, LOS, NN, tamanho, seed):

        if LOS == False:
            k = 0
        else:
            k = 13 - 0.03*d

        PL = -1*self.walfishIkegami(d, LOS)
        h = self.fading(NN, tamanho, seed)

        beta = PL/(1+k)

        h_barra = math.sqrt(k/(1+k))*math.sqrt(PL)

        phi = np.random.uniform(-math.pi, math.pi, 1)

        g = math.sqrt(beta)*h

        v = h_barra * np.exp(1j*phi) + g

        return v
