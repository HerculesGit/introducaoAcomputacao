from tkinter import Tk,PhotoImage, LEFT, RIGHT, Label


raiz = Tk()

textoLabel = Label(raiz,font=('Helvitica',16,'italic'),
	foreground='white',
	background='black',
	padx=20,
	pady=20,
	text='Peace & Love')

minion = PhotoImage(file='minion.gif')
minionLabel = Label(raiz, image=minion)

minionLabel.pack(side=RIGHT)
textoLabel.pack(side=LEFT)
