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
    errores=[]
    # obtenemos errores neurona final y red
    for iteracion in range(iteraciones):
        for i in range(len(entradas)):
            salidas_ocultas=[]
            for neurona in neuronas:
                salida_oculta=neurona.obtener_salida(entradas[i])
                salidas_ocultas.append(salida_oculta)
            
            salida_red=nf.obtener_salida(salidas_ocultas)
            error_red=nf.obtener_error(salidas[i],salida_red)
            errores.append(error_red)
    # ---------------------obtenemos errores neuronas ocultas--------------
            errores_ocultos=[]        
            for j in range(len(neuronas)):
                error_oculto=neuronas[j].obtener_error(nf.pesos[j],error_red,salidas_ocultas[j])
                errores_ocultos.append(error_oculto)
                
    # ---------------------------recalculamos pesos ocultos--------------
            for j in range(len(neuronas)):
                neuronas[j].calcular_nuevos_pesos(entradas[i],errores_ocultos[j])        

    # -----------------------recalculamos pesos finales-------------------
            nf.calcular_nuevos_pesos(error_red,salidas_ocultas)
    
    array=[]
    for i in range(len(entradas)):
        array.append([])
    
    j=0
    for i in range(len(errores)):
        array[j].append(errores[i])
        j+=1
        if j==5:
            j=0
    for element in array:
        plt.plot(element)
    plt.show()
main()  