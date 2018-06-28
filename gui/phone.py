from tkinter import Tk, Label, RAISED
raiz = Tk()
labels = [['1','2','3'],
          ['4','5','6'],
          ['7','8','9'],
          ['*','0','#']]


for r in range(4):		# para cada linha r=0,1,2,3
	for c in range(3):
		label = Label(raiz,
			relief=RAISED,		#borda elevada
			padx=20,			# tornal label largo
			text=labels[r][c])	# texto no label

		# coloca label na linha r e coluna c
		label.grid(row=r, column=c)

