class ColaPrioridad:

    def __init__(self):
        self.vector = []

    def add_element(self, value):
        self.vector.append(value)
        self.flotar(len(self.vector)-1)

    def remove_element(self):
        self.vector[0], self.vector[-1] = self.vector[-1], self.vector[0]
        value = self.vector.pop()
        self.hundir(0)
        return value

    def flotar(self, index):
        while index > 0 and self.vector[index] > self.vector[(index-1)//2]:
            padre = (index-1)//2
            self.vector[index], self.vector[padre] = self.vector[padre], self.vector[index]
            index = padre

    def hundir(self, index):
        hijo_izq = (index*2) + 1
        control = True
        while control and hijo_izq < len(self.vector):
            hijo_der = hijo_izq + 1
            mayor = hijo_izq
            if hijo_der < len(self.vector):
                if self.vector[hijo_der] > self.vector[hijo_izq]:
                    mayor = hijo_der

            if self.vector[index] < self.vector[mayor]:
                self.vector[index], self.vector[mayor] = self.vector[mayor], self.vector[index]
                index = mayor
                hijo_izq = (index*2) + 1
            else:
                control = False


    def size(self):
        return len(self.vector)

    def monticulizar(self):
        for i in range(len(self.vector)):
            self.flotar(i)
    
    def heapsort(self):
        vector = []
        for i in range(len(self.vector)):
            vector.append(self.remove_element())
        return vector

    def arrive(self, value, priority):
        self.add_element([priority, value])

    def attention(self):
        return self.remove_element()