from tkinter import *
import emoji

root = Tk()
root.title("Xadrez")

margem = 100

w = 800
h = 800
x = ((root.winfo_screenwidth())/2) - (w/2)
y = ((root.winfo_screenwidth())/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

canvas = Canvas(root, bg = "brown", width = 800, height = 800)

def Pecas():
	#Brancos
	for coluna in range(0, 2):
		for linha in range(0, 9):
			#Peão
			if (coluna == 1):	
				x = 25 + (linha * margem)
				y = 40 + (coluna * margem)
				peaob = Label(text = "Peão\nBranco", font = "Verdana 7", width = 8).place(x = x, y = y)
			if coluna == 0:
				#Torre
				if ((linha == 0) or (linha == 7)):
					x = 25 + (linha * margem)
					y = 40 + (coluna * margem)
					torreb = Label(text = "Torre\nBranco", font = "Verdana 7", width = 8).place(x = x, y = y)
				#Cavalo
				if ((linha == 1) or (linha == 6)):
					x = 25 + (linha * margem)
					y = 40 + (coluna * margem)
					cavalob = Label(text = "Cavalo\nBranco", font = "Verdana 7", width = 8).place(x = x, y = y)
				#Bispo
				if ((linha == 2) or (linha == 5)):
					x = 25 + (linha * margem)
					y = 40 + (coluna * margem)
					bispob = Label(text = "Bispo\nBranco", font = "Verdana 7", width = 8).place(x = x, y = y)
				#Rainha
				if (linha == 3):
					x = 25 + (linha * margem)
					y = 40 + (coluna * margem)
					rainhab = Label(text = "Rainha\nBranca", font = "Verdana 7", width = 8).place(x = x, y = y)
				#Rei
				if (linha == 4):
					x = 25 + (linha * margem)
					y = 40 + (coluna * margem)
					reib = Label(text = "Rei\nBranco", font = "Verdana 7", width = 8).place(x = x, y = y)


#-------- Mesa {
ajudacor = 0
for coluna in range(0, 9):
	for linha in range(0, 9):
		if ((ajudacor % 2) == 0):
			x = linha * margem
			y = coluna * margem
			mesa1 = canvas.create_rectangle(x, y, x + 100, y + 100, width = 0, fill = "black")
				
		else:
			x = linha * margem
			y = coluna * margem
			mesa2 = canvas.create_rectangle(x, y, x + 100, y + 100, width = 0, fill = "white")
			
		ajudacor += 1

Pecas()
#-------- }

canvas.pack()

#--
root.mainloop()