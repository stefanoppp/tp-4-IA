import math
import numpy as np
class Neurona_oculta:
    def __init__(self,pesos):
        self.pesos=pesos
        self.lr=0.4
        
    def obtener_salida(self,entradas):
        prod_escalar=np.dot(self.pesos,entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def obtener_error(self,peso_entrada_neurona_final,error_red,salida_neurona):
        error=salida_neurona*(1-salida_neurona)*(peso_entrada_neurona_final*error_red)
        return error
        
    def calcular_nuevos_pesos(self,entradas,error_neurona):
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+(self.lr*entradas[i]*error_neurona)
        return self.pesos

    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig