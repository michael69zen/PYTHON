'''PRIMER RETO'''

# 0 = espacio vacío
sudoku = [
    [0,0,0,0,4,0,0,3,8],
    [5,0,8,0,0,0,0,0,0],
    [3,0,9,0,0,8,0,0,4],
    [0,0,0,0,3,9,0,1,0],
    [0,0,5,0,7,0,2,0,3],
    [0,1,3,0,8,2,0,0,0],
    [4,0,0,8,5,0,3,0,0],
    [7,3,6,0,0,0,9,0,5],
    [0,0,0,0,9,3,0,2,7]
]

def valido(f, c, n): #Puedo poner el numero n en la fila f, columna c
    for i in range(9): #Revisa la fila y la columna
        if sudoku[f][i] == n or sudoku[i][c] == n: #Si el numero ya esta en la misma fila o en la misma columna
            return False #Entonces NO se puede poner
    #Revisa el cuadrito 3x3
    f0 = (f // 3) * 3
    c0 = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            if sudoku[f0+i][c0+j] == n: #Si el numero ya esta en ese cuadrito
                return False #No se puede poner

    return True #Si pasa por todo, si se puede poner

def resolver():
    for f in range(9):
        for c in range(9):
            if sudoku[f][c] == 0: #Busca un lugar vacio
                for n in range(1,10): #Prueba del 1 al 9
                    if valido(f, c, n): #Si este numero se puede colocar aqui
                        sudoku[f][c] = n #lo escribe
                        if resolver(): #Sigue resolviendo
                            return True
                        sudoku[f][c] = 0 #Si se equivoca 
                return False #Borra el numero y prueba otro
    return True #Cuando ya no hay 0, Sudoku terminado

resolver()

for fila in sudoku:
    print(fila) #Muestra el resultado
