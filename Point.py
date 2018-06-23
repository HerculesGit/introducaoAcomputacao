class Point:
    'classe que representa pontos no plano'
    
    def __init__(self,coordx=0,coordy=0):
        'construtor com parâmetro'
        self.x = coordx
        self.y = coordy

    def setx(self, coordx):
        'define coordenada x do ponto como coordx'
        self.x = coordx

    def sety(self, coordy):
        'define coordenada y do ponto como coordy'
        self.y = coordy
    
    def get(self):
        'retorna tupla com coordenadas x e y do ponto'
        return (self.x, self.y)

    def move(self, dx, dy):
        'muda as coordenadas x e y por dx e dy'
        self.x += dx
        self.y += dy

    def __repr__(self):
        return 'Ponto ({}, {})'.format(self.x,self.y)

    def __str__(self):
        return 'Ponto ({}, {})'.format(self.x,self.y)

    def __eq__(self, outro):
        'self == outro quando eles têm as mesmas coordenadas'
        return (self.x == outro.x) and (self.y == outro.y)
    


class Retangulo:
    
    def setTamanho(self,base,altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        'fórmula = 2*(b+a)'
        return 2*(self.base + self.altura)

    def area(self):
        'fórmula = base * altura'
        return self.base * self.altura 



class Animal:
    'define a especie do animal'
    def setEspecie(self, especie):
        self.esp = especie

    def setLinguagem(self, linguagem):
        'define a linguagem do animal'
        self.ling = linguagem

    def fala(self):
        ' exibe uma sentença pelo animal'
        print('Eu sou um {} e sei {}'.format(self.esp,self.ling))



class Ave(Animal):

    def fala(self):
        print('{}! '.format(self.ling) * 3)













        
