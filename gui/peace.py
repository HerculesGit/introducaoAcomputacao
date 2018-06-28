from tkinter import Tk, Label, PhotoImage

raiz = Tk()

#transforma GIF em formato que o tkinter pode exibir
photo = PhotoImage(file='minion.gif')

peace = Label(master=raiz,
	
	width=1800,
	height=1800)

peace.pack()
raiz.mainloop()