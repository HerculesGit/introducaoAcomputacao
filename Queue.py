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
	    #raise é uma palavra-chave que levanta a instrução colocada pelo construtor
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

    def __getitem__(self,chave):
        'com isso poderemos usar o operador de indexaçao []'
        #agora tbm poderemos usar o for-each
        return self.q[chave]
    
    def __setitem__(self,chave,item):
        self.q[chave] = item

    def __iter__(self):
        'retorn iterador de Queue'
        return QueueIterator(self)


class EmptyQueueError(Exception):
    pass

class QueueIterator:
    'iterador para a classe de contêiner Queue'

    def __init__(self,q):
        'costrutor'
        self.indice = len(q)-1
        self.q = q

    def __next__(self):
        '''retorna o próximo item de Queue; se não houver item
            seguinte, levanta exceção StopIteration '''
        if self.indice < 0:
            raise StopIteration()

        res = self.q[self.indice]
        self.indice -=1
        return res
        
