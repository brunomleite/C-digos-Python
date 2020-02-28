from tkinter import *
from random import randint
from tkinter import messagebox

root = Tk()
canvas = Canvas(width = 400, height = 400)
root.title("Tabuleiro :D")  # Nao mexer no tamanho da janela
w = 400
h = 400
x = ((root.winfo_screenwidth()) / 2) - (w / 2)
y = ((root.winfo_screenheight()) / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # janela sempre aparece no meio da tela

background = canvas.create_rectangle(0,0,400,400,fill='black')

#Tabuleiro----------------------------------------------------------------------
lista = [1,20,19,18,17,16,2,15,3,14,4,13,5,12,6,7,8,9,10,11] #ordem dos quadrados do tabuleiro de acordo com a sua criação
position = []
venenoA = []
for i in range(6):
    for j in range(6):
        if i != 0 and i != 5 and (j in [1,2,3,4]):
            pass
        else:
            position.append([(50*(i+1))+5,(50*(i+1))+45]) #coloacandos o x incial e final da posição
            position.append([50*(j+1)+5, (50*(j+1))+45])  # mesmo pro y
            canvas.create_rectangle((50*(i+1)),50*(j+1),(50*(i+1))+50,(50*(j+1))+50, outline='white') #criando quadrado
for i in range(20):
    position.insert((3*i+2),lista[i]) #organizando o tabuleiro para o player andar na ordem que eu quero
for i in range(5):
    venenoA.append(randint(1,20))
print(venenoA)

#Andar--------------------------------------------------------------------------
fim = True
place = [1] #posição do player
place2 = [2]
turno = [1]
antidoto = [1]
antidoto2 = [1]
veneno = False
veneno2 = False

'''for i in range(20):
    print(position[(3*i)+0],position[(3*i)+1],position[(3*i)+2]) #só printando as posições'''

player = canvas.create_oval(55,55,95,95, fill='red') #criar player
player2 = canvas.create_oval(105,55,145,95, fill='blue')
t = canvas.create_text(200,375,fill="red",font="Times 18 bold", text = "Turno Player" + str(turno[0]))

def andar():
    global veneno
    global veneno2
    if turno[0] == 1:
        dado = randint(1,6)
        if veneno == False:
            place[0] = place[0] + dado
        else:
            place[0] = place[0] + (dado - 2)
        print(dado)
        for i in range(20):
            if position[(3*i)+2] == place[0] and place[0] < 20:
                if place[0] == place2[0]:
                    place[0] = place[0] + 1
                    for i in range(20):
                        if position[(3*i)+2] == (place[0]):
                            canvas.coords(player, position[(3 * i)][0], position[(3 * i + 1)][0], position[(3 * i)][1], position[(3 * i + 1)][1])
                else:
                    #modificando a posição do player
                    canvas.coords(player, position[(3 * i)][0], position[(3 * i + 1)][0], position[(3 * i)][1], position[(3 * i + 1)][1])
                if position[(3 * i) + 2] in venenoA:
                    veneno = True
                    canvas.itemconfig(player, width=2)
                    canvas.itemconfig(player, outline='green')
                    messagebox.showinfo("Veneno", "P1 Você está envenenado!")
        if place[0] >= 20:
            canvas.coords(player, position[(3 * 1)][0], position[(3 * 1 + 1)][0], position[(3 * 1)][1],
                              position[(3 * 1 + 1)][1])
            messagebox.showinfo("Win", "P1 você chegou ao final!!!")
        turno[0] = 2
        canvas.itemconfig(t, text="Turno Player" + str(turno[0]))
        canvas.itemconfig(t, fill = 'blue')
    elif turno[0] == 2:
        dado = randint(1, 6)
        if veneno2 == False:
            place2[0] = place2[0] + dado
        else:
            place2[0] = place2[0] + (dado - 2)
        print(dado)
        for i in range(20):
            if position[(3 * i) + 2] == place2[0] and place2[0] < 20:
                # modificando a posição do player
                if place2[0] == place[0]:
                    place2[0] = place2[0] + 1
                    for i in range(20):
                        if position[(3 * i) + 2] == (place2[0]):
                            canvas.coords(player2, position[(3 * i)][0], position[(3 * i + 1)][0], position[(3 * i)][1], position[(3 * i + 1)][1])
                else:
                    # modificando a posição do player
                    canvas.coords(player2, position[(3 * i)][0], position[(3 * i + 1)][0], position[(3 * i)][1], position[(3 * i + 1)][1])
                if position[(3 * i) + 2] in venenoA:
                    veneno2 = True
                    canvas.itemconfig(player2, width=2)
                    canvas.itemconfig(player2, outline='green')
                    messagebox.showinfo("Veneno", "P2 Você está envenenado!")
        if place2[0] >= 20:
            canvas.coords(player2, position[(3 * 1)][0], position[(3 * 1 + 1)][0], position[(3 * 1)][1], position[(3 * 1 + 1)][1])
            messagebox.showinfo("Win", "P2 você chegou ao final!!!")
        turno[0] = 1
        canvas.itemconfig(t, text="Turno Player" + str(turno[0]))
        canvas.itemconfig(t, fill='red')

#veneno
def curar():
    global veneno
    global veneno2
    if turno[0] == 1:
        if antidoto[0] > 0:
            if veneno == True:
                antidoto[0] = antidoto[0] - 1
                veneno = False
                canvas.itemconfig(player, outline='red')
                messagebox.showinfo("Cura", "P1 Curado!")
            elif veneno == False:
                antidoto[0] = antidoto[0] - 1
                messagebox.showinfo("Cura", "P1 Desperdiçou Antidoto!")
        else:
            messagebox.showinfo("Cura", "P1 não possui mais antidotos!")
        turno[0] = 2
        canvas.itemconfig(t, text="Turno Player" + str(turno[0]))
        canvas.itemconfig(t, fill='blue')
    elif turno[0] == 2:
        if antidoto2[0] > 0:
            if veneno2 == True:
                antidoto2[0] = antidoto2[0] - 1
                veneno2 = False
                canvas.itemconfig(player2, outline='blue')
                messagebox.showinfo("Cura", "P2 Curado!")
            elif veneno2 == False:
                antidoto2[0] = antidoto2[0] - 1
                messagebox.showinfo("Cura", "P2 Desperdiçou Antidoto!")
        else:
            messagebox.showinfo("Cura", "P2 não possui mais antidotos!")
        turno[0] = 1
        canvas.itemconfig(t, text="Turno Player" + str(turno[0]))
        canvas.itemconfig(t, fill='red')

while fim == True:
    # botão de andar :D
    walkButton = Button(text="Andar",
                        font="Verdana 8",
                        width="10",
                        background="white",
                        command=andar)
    walkButton.place(x=80, y=20)

    # botão de tomar antidoto :D
    walkButton = Button(text="Tomar Antidoto",
                        font="Verdana 8",
                        width="16",
                        background="white",
                        command=curar)
    walkButton.place(x=200, y=20)
    print(turno[0])

    canvas.pack()
    root.mainloop()


