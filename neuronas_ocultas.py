import math
import numpy as np
class Neurona_oculta:
    def __init__(self,pesos):
        self.pesos=pesos
        self.lr=0.5
        
    def obtener_salida(self,entradas):
        prod_escalar=np.dot(self.pesos,entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def obtener_error(self,peso_entrada_neurona_final,error_red,entradas):
        salida_real=self.obtener_salida(entradas)
        error=salida_real*(1-salida_real)*(peso_entrada_neurona_final*error_red)
        return error
        
    def calcular_nuevos_pesos(self,error_capa_oculta,peso_capa_oculta,entradas):
        salida_real=self.obtener_salida(entradas)
        error=salida_real*(1-salida_real)*(error_capa_oculta*peso_capa_oculta)
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+(self.lr*entradas[i]*error)
        return self.pesos

    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig