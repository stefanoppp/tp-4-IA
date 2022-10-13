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
    # generamos neuronas con 3 pesos cada una
    for i in range(cant_neuronas):
        pesos_random=[]
        for j in range(3):
            peso_random=random.random()
            pesos_random.append(peso_random)
        n=Neurona_oculta(pesos_random)
        neuronas.append(n)
    
    # comienza la iteracion
    for i in range(iteraciones):
        print(i)
main()