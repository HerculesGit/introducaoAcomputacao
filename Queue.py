class Queue:
    'uma classe de fila clássica'

    def __init__(self, q = None):
        'inicializa fila com base na lista q, padrão é fila vazia '
        if q == None:
            self.q = []
        else:
            self.q = q

    def enqueue(self,item):
        'Coloca um elemento na cauda da fila'
        return self.q.append(item)

    def dequeue(self):
        'remove um elemento no começo da fila e retorna ele'
        if len(self.q) == 0:
            raise EmptyQueueError(' remoção de uma fila vazia')
        return self.q.pop(0)

    def isEmpty(self):
        'true = sem elemento ; false = tem elemento'
        return (len(self.q) == 0)

    def __eq__(self,outro):
        'self == outro ter os mesmos elementos'
        return self.q == outro.q

    def __len__(self):
        'retorna número de itens na fila'
        return len(self.q)
        
    def __repr__(self):
        return '{}'.format(self.q)


class EmptyQueueError(Exception):
    pass

