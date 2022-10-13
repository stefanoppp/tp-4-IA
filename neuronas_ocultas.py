import math
import numpy as np
class Neurona_oculta:
    def __init__(self,pesos):
        self.pesos=pesos
        self.lr=0.5
        
    def obtener_salida(self,entrada):
        prod_escalar=np.dot(self.pesos,entrada)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def obtener_error(self,peso_entrada_neurona_final,error_red,entrada):
        salida_real=self.obtener_salida(entrada)
        error=salida_real*(1-salida_real)*(peso_entrada_neurona_final*error_red)
        return error
        
    def calcular_nuevos_pesos(self,error_capa_oculta,peso_capa_oculta):
        salida_real=self.obtener_salida()
        error=salida_real*(1-salida_real)*(error_capa_oculta*peso_capa_oculta)
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+(self.lr*self.entradas[i]*error)
        return self.pesos

    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig