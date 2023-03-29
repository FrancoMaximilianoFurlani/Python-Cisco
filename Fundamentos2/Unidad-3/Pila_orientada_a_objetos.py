class Stack:
    def __init__(self): # inlicializa con una lista que sera nuerta pila 
        self.__stack_list = []


    def push(self, val): # tomara un valor ( val ) para apregarlo con el metodos append de listas 
        self.__stack_list.append(val)


    def pop(self): # pop() elimina y retorna el último elemento de la lista
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack() # este es un objeto

stack_object.push(3) # aca agraga un elemento en el ultimo lugar de la lista 
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop()) # muestra el ultimo elemento y lo borra dejando en el ultimo lugar al anterior
print(stack_object.pop())
print(stack_object.pop())
