#1 célula muerta con 3 vecinas vivas se enciende
#1 célula viva con 2 o 3 vecinas vivas sigue viva, en otro caso muere

import numpy as np
import random
import time



def gen(tablero):
    for i in range(len(tablero)):

        for j in range(len(tablero)):

            num = random.randint(0,100)

            if num > 70:

                tablero[i,j] = 1


def check(tablero, i, j):
    num_celdas = 0
    if i != 0:
        num_celdas += tablero[i-1, j] #Arriba
        if j != len(tablero) - 1 :
            num_celdas += tablero [i -1, j +1] #Arriba a la derecha
        if j != 0:
            num_celdas += tablero [i-1, j-1] #Arriba a la izquierda
    
    if i != len(tablero) -1 :
        num_celdas += tablero[i + 1, j] #Abajo
        if j != len(tablero) -1 :
            num_celdas += tablero [i+1, j +1] #Abajo a la derecha
        if j != 0:
            num_celdas += tablero [i + 1, j -1] #Abajo a la izquierda

    if j  != len(tablero) - 1  :
        num_celdas += tablero[i, j +1]
    if j != 0:
        num_celdas += tablero[i, j -1]

    return num_celdas


def step(tablero):

    for i in range(len(tablero)):

        for j in range(len(tablero)):

            if tablero[i,j] == 0:
                
                vivas = check(tablero, i,j)

                if vivas == 3:
                    tablero[i,j] = 1
            
            if tablero [i,j] == 1:

                vivas = check(tablero,i,j)

                if vivas == 2 or vivas ==3:
                    tablero[i,j] = 1
                else:
                    tablero [i,j] = 0

def print_tablero(tablero):

    print("\n\n\n\n\n")

    for i in range(len(tablero)):

        for j in range(len(tablero)):

            if tablero[i,j] == 0:
                print(" ", end = "")
            else:
                print("*", end ="")
        print("")
  


                
                

tablero = np.zeros((20,20))
gen(tablero)
print_tablero(tablero)

for i in range(1000000):

    step(tablero)
    print_tablero(tablero)
    time.sleep(0.7)