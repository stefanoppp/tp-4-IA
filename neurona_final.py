import math
import numpy as np
class Neurona_final:
    def __init__(self,pesos,salida,entradas):
        self.pesos=pesos
        self.entradas=entradas
        self.salida=salida
        self.lr=0.5
    
    def obtener_salida(self):
        prod_escalar=np.dot(self.pesos,self.entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def obtener_error(self):
        salida_obtenida=self.obtener_salida()
        error=salida_obtenida*(1-salida_obtenida)*(self.salida-salida_obtenida)
        return error
        
    def calcular_nuevos_pesos(self,error):
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+(self.lr*self.entradas[i]*error)
        return self.pesos

    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig