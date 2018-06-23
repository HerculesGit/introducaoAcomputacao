class Queue2(list):
    'uma classe de fila, subclasse de list'
    
    def enqueue(self,item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    def isEmpty(self):
        return (len(self) == 0)
