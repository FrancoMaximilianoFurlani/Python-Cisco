
#esta clase crea un lista llamada pila (stack)

# class Stack:
#     def __init__(self):
#         self.stack_list = []


# stack_object = Stack()
# print(len(stack_object.stack_list))

# mismo codigo pero de manera encasulada solo se puede operar desde adentro  por los dos __ antes del metodo 
# todos los metodos se vuelven privados

class Stack:
    def __init__(self):
        self.__stack_list = []


stack_object = Stack()
print(len(stack_object.__stack_list))
