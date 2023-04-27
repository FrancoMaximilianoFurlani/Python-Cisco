count = 0
height =0
def tomar_bloques():
    
    bloques = int(input("Ingresa el número de bloques: "))

    return bloques

def calcular_altura(blocks):

    while blocks>0:
        
        count+=1
        blocks-=count
        if blocks >= height:
            height+=1
            
    return height

altura = calcular_altura(tomar_bloques())

print("La altura de la pirámide:", altura)
