import numpy as np


class Metrics:

    def data_rate_r1(w,B,p1,gama1,N0):
        num = p1*gama1

        den = (w*N0*B) 

        r1 = w*B*np.log2(1+(num/den))

        return r1

    def data_rate_r2(w,B,p2,gama2,p1,N0):
        num = p2*gama2

        den = (p1*gama2)+(w*N0*B) 

        r2 = w*B*np.log2(1+(num/den))

        return r2


    def data_rate_r3(w,B,p3,gama3,p1,p2,N0):
        num = p3*gama3

        den = (p1*gama3)+(p2*gama3)+(w*N0*B) 

        r3 = w*B*np.log2(1+(num/den))

        return r3

    def data_rate_r4(w,B,p4,gama4,p1,p2,p3,N0):
        num = p4*gama4

        den = (p1*gama4)+(p2*gama4)+(p3*gama4)+(w*N0*B)  

        r4 = w*B*np.log2(1+(num/den))

        return r4

    def data_rate_r5(w,B,p5,gama5,p1,p2,p3,p4,N0):
        num = p5*gama5

        den = (p1*gama5)+(p2*gama5)+(p3*gama5)+(p4*gama5)+(w*N0*B) 

        r5 = w*B*np.log2(1+(num/den))

        return r5

    def data_rate_r6(w,B,p6,gama6,p1,p2,p3,p4,p5,N0):  
        num = p6*gama6

        den = (p1*gama6)+(p2*gama6)+(p3*gama6)+(p4*gama6)+(p5*gama6)+ (w*N0*B)

        r6 = w*B*np.log2(1+(num/den))

        return r6