import numpy as np
import math
import random

class Coeficiente_de_Desvanecimento:

    def gcanal(self, NN=None, SEED=None):

        np.random.seed(SEED)

        RAND_MAX = 32767.0
        fdmax = 10.0
        fs = 10.0**4
        ud = np.zeros((1, NN))
        ua = np.zeros((1, NN))

        for j in range(NN):
            ud[:, j] = np.random.randint(0, RAND_MAX, size=1)/RAND_MAX
            ua[:, j] = np.random.randint(0, RAND_MAX, size=1)/RAND_MAX

        dn = np.zeros((1, NN))
        an = np.zeros((1, NN), dtype=complex)
        for j in range(NN):
            dn[:, j] = fdmax*np.cos(2.0*np.pi*ud[:, j])
            rel = np.cos(2.0*np.pi*ua[:, j])
            img = np.sin(2.0*np.pi*ua[:, j])
            an[:, j] = rel + 1j*img
        T = 1.0/fs
        doppler = np.zeros((1, NN))
        for j in range(NN):
            doppler[:, j] = 2.0*np.pi*T*dn[:, j]
        return an, doppler

    def gera_canal(self, NN=None, conc=None, an=None, doppler=None):

        e = np.zeros((1, NN), dtype=complex)
        h = np.zeros((1, NN), dtype=complex)
        h_n = np.zeros((1, 1), dtype=complex)

        for j in range(NN):
            rel = np.cos(conc*doppler[:, j])
            img = np.sin(conc*doppler[:, j])
            e[:, j] = rel+1j*img
            h[:, j] = an[:, j]*e[:, j]

        h_n = np.sum(h)
        h_n = (1.0/np.sqrt(NN))*h_n

        return h_n

    def fading(self,NN=None,tamanho=None, seed=None):
        h = np.zeros((1, tamanho), dtype=complex)
        conc = 1.0
        an, doppler = self.gcanal(NN, seed)
        for j in range(tamanho):
            h[:, j] = self.gera_canal(NN, conc, an, doppler)
            conc = conc+1.0
        return h

    # d é dado em metros
    def hatacost231(self, d=None,fc=None):
        ### em metros
        ht = 30
        hr = 2  

        alpha=  (1.1*(math.log(fc, 10)) - 0.7)*hr   -  (1.56*(math.log(fc, 10) - 0.8))  

        # medida em dB, centros metropolitano Cm = 3 dB, c.c. Cm = 0 dB
        cm = 3       
        
        L = 46.3 + (33.9*(math.log(fc, 10))) - (13.82*(math.log(ht, 10))) - alpha +\
               (44.9 - (6.55*(math.log(ht, 10))))*(math.log(d/1000, 10)) + cm

        PL = -L

        return PL

    # d é dado em mestros
    def walfishikegami(self, d=None, LOS=None, fc=None):
        if LOS == True:
            PL = 35.4-(26*math.log(d, 10)) - (20*math.log(fc, 10))
        else:
            PL = 55.9 - (38*math.log(d, 10)) - \
                ((24.5 + ((1.5*fc)/925))*math.log(fc, 10))

        return PL

    def desvanecimentoglobal(self,d=None, LOS=None, NN=None, tamanho=None, seed=None,fc=2000):
        
        h = self.fading(NN, tamanho, seed)
        #PL =  self.walfishikegami(d, LOS,fc)
        PL = self.hatacost231(d,fc)

        if LOS == False:
            k = 0
            PL = 10**(PL*0.1)
            beta = PL/(1+k)
            

            g = math.sqrt(beta)*h
            v = g

        else:
            k = 13 - 0.03*d

           
            beta = PL/(1+k)
           

            g = math.sqrt(beta)*h

            h_barra = math.sqrt(k/(1+k))*math.sqrt(PL)

            phi = np.random.uniform(-math.pi, math.pi, 1)

            v = h_barra * np.exp(1j*phi) + g

        return v
