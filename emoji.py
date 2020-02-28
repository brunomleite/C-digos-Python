from tkinter import *
import emoji

root = Tk()
root.title("Emoji")

w = 600
h = 600
x = ((root.winfo_screenwidth())/2) - (w/2)
y = ((root.winfo_screenheight())/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

canvas = Canvas(root, bg = "brown", width = 600, height = 600)

texto = (emoji.emojize("This App is :star:", use_aliases = True))
teste = Label(text = texto).place(x=10,y=50)



canvas.pack()

print(emoji.emojize("Consegui fodido :sunglasses:", use_aliases = True))

#--
root.mainloop()