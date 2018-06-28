from tkinter import Tk, Label, PhotoImage

raiz = Tk()

#transforma GIF em formato que o tkinter pode exibir
photo = PhotoImage(file='minion.gif')

minion = Label(master=raiz,
	image=photo,
	width=1300,
	height=800)

minion.pack()
i = 0 

while i<5:
	i+=1
	print(i)

#raiz.mainloop()
