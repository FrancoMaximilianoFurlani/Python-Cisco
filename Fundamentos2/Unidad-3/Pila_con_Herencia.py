class Stack: # creamos una clase pila con sus metodos 
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack): # creamos una nueva Clase pila que hera los metodos de la clase pila original
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0 # inlicializa un contador

    def get_sum(self):
        return self.__sum

    def push(self, val): # invoca la  clase pila original para segur operando la pila y agraga un metodo de incremento 
        self.__sum += val
        Stack.push(self, val)

    def pop(self): # invoca la  clase pila original para segur operando la pila y agraga un metodo de decremento 
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
