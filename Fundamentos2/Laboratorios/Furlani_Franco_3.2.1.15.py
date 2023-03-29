# 3.2.1.15 Colas alias FIFO

class Queue: # crea una lista de objestos 
    def __init__(self):
        self.stacklist = []

    def put(self, elem): # carga los elementos en la lista
        self.stacklist.append(elem)

    def get(self): 
        elem = self.stacklist[0] # toma el primer elemento de la lista lo asigna a una variable 
        del self.stacklist[0] # borra el elemento de la lista 
        return elem # retona la variable


# esta clase estaba el princio del codigo para poder trabajarlo de manera organizana lo movimos aca 

class QueueError(Queue): # si cae en una lista vacia imprimira un mensaje de error
    def __init__(self,Queue):
        Queue.__init__(self)
        print("Error de Cola")
    


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    QueueError(Queue) # corregimos el codigo para que cuando ingrese un error ingrese a la clase QueueError
