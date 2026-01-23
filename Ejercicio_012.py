def es_cuadrado_perfecto(n):
    if n<0:
        return False
    
    raiz = int(n**0.5)
    return raiz*raiz==n

h = es_cuadrado_perfecto(9)
print(h) 
