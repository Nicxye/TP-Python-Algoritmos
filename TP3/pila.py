class Pila():
    def __init__(self):
        self.__elements = []
    
    def on_top(self):
        if (self.size() > 0):
            return self.__elements[-1]
        
    def pop(self):
        if self.size() > 0:
            return self.__elements.pop()
        
    def push(self, value):
        self.__elements.append(value)
    
    def size(self):
        return len(self.__elements)
