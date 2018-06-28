from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE

raiz = Tk()


# label com texto "A paz coma com um sorriso"
texto = Label(raiz,
	font = ("Helvitica",16, "bold italic"),
	foreground= "white", 	#cor da letra
	background='black', 	#cor do fundo
	padx=25,	#expande label 25 pixels para esquerda
	pady=10,	# amplia label 10 pixels acima e abaixo
	text="A Paz começa com um sorriso.")

texto.pack(side=BOTTOM)	#empurra o label para baixo

#label com imagem de símbolo de paz
minion = PhotoImage(file='minion.gif')
minionLabel = Label(raiz,
	borderwidth=12,	# largura da borda do label
	relief=RIDGE,	# estilo da borda do label
	image=minion)

minionLabel.pack(side=LEFT)	# empura o label para esquerda


#label com a imagem da carinha sorridente
smiley = PhotoImage(file='Smiley-11-icon.png')
smileyLabel = Label(raiz,
	image=smiley)

smileyLabel.pack(side=RIGHT)

#root.mainloop()
