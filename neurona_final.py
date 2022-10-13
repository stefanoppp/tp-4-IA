import math
import numpy as np
class Neurona_final:
    def __init__(self,pesos):
        self.pesos=pesos
        self.lr=0.5
    
    def obtener_salida(self,entradas):
        prod_escalar=np.dot(self.pesos,entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def obtener_error(self,entradas,salida):
        salida_obtenida=self.obtener_salida(entradas)
        error=salida_obtenida*(1-salida_obtenida)*(salida-salida_obtenida)
        return error
        
    def calcular_nuevos_pesos(self,error_red,entradas):
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+(self.lr*entradas[i]*error_red)
        return self.pesos

    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig