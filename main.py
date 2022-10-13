from neurona_final import Neurona_final
from neuronas_ocultas import Neurona_oculta
import matplotlib.pyplot as plt
import random
def main():
    
    entradas=[[1,0,0],
              [1,1,1],
              [0,1,1],
              [0,0,0],
              [0,0,1]]
    
    salidas=[1,0,0,0,1]
    
    cant_neuronas=int(input("Digite cantidad de neuronas: "))
    iteraciones=int(input("Digite cantidad de iteraciones: "))
    
    neuronas=[]
    # generamos neuronas ocultas con 3 pesos c/u
    for i in range(cant_neuronas):
        pesos_neuronales=[]
        for j in range(3):
            peso_random=random.random()
            pesos_neuronales.append(peso_random)
        n=Neurona_oculta(pesos_neuronales)
        neuronas.append(n)
    
    # generamos neurona final con 1 peso por cada neurona generada
    pesos_finales=[]
    for j in range(len(neuronas)):
        peso_random=random.random()
        pesos_finales.append(peso_random)
    nf=Neurona_final(pesos_finales)

    # ------------------comienza la iteracion------------------
    
    for i in range(iteraciones):
        for j in range(len(entradas)):
            salidas_ocultas=[]
            # ---------------------obtengo salidas de capa oculta---------------------
            for k in range(len(neuronas)):
                salida=neuronas[k].obtener_salida(entradas[j])
                salidas_ocultas.append(salida)
            
            error_red=nf.obtener_error(salidas_ocultas,salidas[j])   
            
            # ------------------------obtengo los errores ocultos--------------------
            errores_ocultos=[]
            for l in range(len(neuronas)):
                error_oculto=neuronas[l].obtener_error(nf.pesos[l],error_red,entradas[j])
                errores_ocultos.append(error_oculto)
           
        #    --------------------------recalculamos pesos ocultos----------------------
            for m in range(len(neuronas)):
                neuronas[m].pesos=neuronas[m].calcular_nuevos_pesos(errores_ocultos[m],pesos_finales[m],entradas[j])
            
            # ------------------recalculamos pesos finales------------------------  
            nf.pesos=nf.calcular_nuevos_pesos(error_red,salidas_ocultas)
main()  