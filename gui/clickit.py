from tkinter import Tk, Button
from time import strftime, localtime
from tkinter.messagebox import showinfo 

# nome da funcao fi definida abaixo
def clicked():
	'exibe informação de die e hora'
	hora = strftime('Dia: %d %b %Y \nHora: %H:%M:%S %p\n',
		localtime())
	showinfo(message=hora)

raiz = Tk()

# cria botão rotulado com 'Clique aqui' e manipulador de evendo clicked()
button = Button (raiz,
	text='Clique aqui',
	command=clicked)		# manipulador de evento clique do botao

button.pack() 				# posicionado-o na raiz
