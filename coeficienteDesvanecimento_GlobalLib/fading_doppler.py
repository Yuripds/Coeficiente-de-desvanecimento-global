import numpy as np
import random


class Fading_Doppler:

    def gcanal(self, NN, SEED):

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

    def gera_canal(self, NN, conc, an, doppler):

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
