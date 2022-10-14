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
    peso_1=[]
    peso_2=[]
    peso_3=[]
    historial_pesos_finales=[]
    historial_pesos_finales.append(pesos_finales)
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
            # --------------------------recalculamos pesos finales------------------------  
            nf.pesos=nf.calcular_nuevos_pesos(error_red,salidas_ocultas)
            historial_pesos_finales.append(nf.pesos)
            # ---------------------------------Graficamos todo---------------------------
            
            for neurona in neuronas:
                pesos_1_neurona=[]
                pesos_2_neurona=[]
                pesos_3_neurona=[]
                for p in range(len(neurona.pesos)):
                    if p==0:
                        pesos_1_neurona.append(neurona.pesos[p])
                    if p==1:
                        pesos_2_neurona.append(neurona.pesos[p])
                    if p==2:
                        pesos_3_neurona.append(neurona.pesos[p])
                peso_1.append(pesos_1_neurona)
                peso_2.append(pesos_2_neurona)
                peso_3.append(pesos_3_neurona)
    
    array=[]
    # -----------------------------------PESOS 1-----------------------------
    for i in range(len(neuronas)):
        array.append([])
    
    h=0
    
    for j in range(len(peso_1)):
        array[h].append(peso_1[j])
        h+=1
        if h==len(neuronas):
            h=0
    
    for element in array:
        plt.plot(element)
    
# --------------------------------------PESOS 2----------------------------
    array=[]
    # graficar pesos ocultos
    for i in range(len(neuronas)):
        array.append([])
    
    h=0
    
    for j in range(len(peso_2)):
        array[h].append(peso_2[j])
        h+=1
        if h==len(neuronas):
            h=0
    
    for element in array:
        plt.plot(element)
        
# ---------------------------------------PESOS 3---------------------------
    array=[]
    # graficar pesos ocultos
    for i in range(len(neuronas)):
        array.append([])
    
    h=0
    
    for j in range(len(peso_3)):
        array[h].append(peso_3[j])
        h+=1
        if h==len(neuronas):
            h=0
    
    for element in array:
        plt.plot(element)
    # ---------------------------------- PESOS FINALES -------------------
    array=[]
    for i in range(len(neuronas)):
        array.append([])
    
    h=0
    for j in range(len(neuronas)):
        array[h].append(pesos_finales[j])
        h+=1
        if h==len(neuronas):
            h=0
    for element in array:
        plt.plot(element)    
    plt.show()        
main()  