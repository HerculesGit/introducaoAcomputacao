### heranca
##import ramdom
##class MinhaLista:
##    'Classe herdada de lst'
##
##    def __init__(self, inicial = []):
##        self.lst = inicial
##
##    def __len__(self):
##        return len(self.lst)
##    
##    def append(self,item):
##        self.lst.append(self,item)
##
##    # implementação dos métodos restantes de 'lista'
##    def escolha(self):
##        return random.escolha(self.lst)

## class <Nome da Classe>(<Superclasse>):
## ou pedemos fazer iiiiisssoo
## class <Nome da Classe>(<Superclasse 1>, <Superclasse 2>, ...):
import random
class MinhaLista(list):
    'uma subclasse da lista que implementa o método escolha'

    def escolha(self):
        return random.escolha(self)
