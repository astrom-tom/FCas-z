from scipy import integrate
import numpy
from decimal import *


class Cosmology:    
    
    def __init__(self, Ho, Omega_m, Omega_L, Omega_K): 
        self.Ho = Ho         
        self.Omega_m = Omega_m
        self.Omega_L = Omega_L
        self.Omega_k = Omega_K
        self.c = 299792458

        self.km_to_mpc = 3.24e-20
        self.sec_to_Gyr = 3.15e16

    def Hubbletime(self, ):
        return 1/(self.Ho*self.km_to_mpc)

    def Hubbledistance(self, ):
        return self.c/(self.Ho*self.km_to_mpc)

    def E(self, z):
        return numpy.sqrt(self.Omega_m*(1+z)**3 + self.Omega_k*(1+z)**2 + self.Omega_L)

    def H(self, z):
        H = self.Ho * self.E(z)
        return H

    def Age_Universe(self, z):

        A_int= lambda x: 1/((1+x)*self.E(x))
        Age_un=integrate.quad(A_int,z,numpy.inf) 
        A=float(Decimal(self.Hubbletime())*Decimal(Age_un[0])/Decimal(self.sec_to_Gyr))

        return A

    def dcE(self, z):
        D_int = lambda x: 1/self.E(x)
        Dc_in = integrate.quad(D_int,0,z)
        co_dist = self.Hubbledistance()*Dc_in[0] * self.km_to_mpc * 1e-3 ##to meter

        return co_dist 

    def dl(self, z):
        da=(1/(1+z))*self.dcE(z)
        dl=(1+z)*(1+z)*da
        return dl 

    def da(self, z):
        da=(1/(1+z))*self.dcE(z)
        return da

    

