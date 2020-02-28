from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#------------------------------------------------
root = Tk()
root.title("Desafio 01")
w = 400
h = 500
x = ((root.winfo_screenwidth())/2) - (w/2)
y = ((root.winfo_screenheight())/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#------------------------------------------------
listaVertices = []
matrizLigacoes = []
for linha in range(10):
    linha = []
    for coluna in range(10):
        linha.append(0)
    matrizLigacoes.append(linha)
print(matrizLigacoes)

maxV = 10
x = [190,130,250,90,290,90,290,130,250,190]
y = [200,230,230,280,280,325,325,370,370,400]

def adicionaVertice():
    global maxV
    fim = False
    if maxV > 0:
        for i in listaVertices:
            if v.get() == i:
                messagebox.showinfo("Alerta", "Vértice Já Existente")
                fim = True

        if fim == False:

            listaVertices.append(v.get())
            print(listaVertices)
            if maxV == 10:
                canvas.create_oval(x[0], y[0], x[0]+20, y[0]+20, fill="#0094e7")  # 1
                um = Label(text = listaVertices[0],
                           font = "Verdana 7",
                           width = 8).place(x=x[0]-18,y=y[0]-22)
            if maxV == 9:
                canvas.create_oval(x[1], y[1], x[1]+20, y[1]+20, fill="#0094e7")  # 2
                dois = Label(text=listaVertices[1],
                           font="Verdana 7",
                           width=8).place(x=x[1] - 22, y=y[1] - 22)
            if maxV == 8:
                canvas.create_oval(x[2], y[2], x[2]+20, y[2]+20, fill="#0094e7")  # 3
                tres = Label(text=listaVertices[2],
                           font="Verdana 7",
                           width=8).place(x=x[2] - 18, y=y[2] - 22)
            if maxV == 7:
                canvas.create_oval(x[3], y[3], x[3]+20, y[3]+20, fill="#0094e7")  # 4
                quatro = Label(text=listaVertices[3],
                           font="Verdana 7",
                           width=8).place(x=x[3] - 32, y=y[3] - 22)
            if maxV == 6:
                canvas.create_oval(x[4], y[4], x[4]+20, y[4]+20, fill="#0094e7")  # 5
                cinco = Label(text=listaVertices[4],
                           font="Verdana 7",
                           width=8).place(x=x[4], y=y[4] - 22)
            if maxV == 5:
                canvas.create_oval(x[5], y[5], x[5]+20, y[5]+20, fill="#0094e7")  # 6
                seis = Label(text=listaVertices[5],
                           font="Verdana 7",
                           width=8).place(x=x[5] - 58, y=y[5])
            if maxV == 4:
                canvas.create_oval(x[6], y[6], x[6]+20, y[6]+20, fill="#0094e7")  # 7
                sete = Label(text=listaVertices[6],
                           font="Verdana 7",
                           width=8).place(x=x[6] + 22, y=y[6])
            if maxV == 3:
                canvas.create_oval(x[7], y[7], x[7]+20, y[7]+20, fill="#0094e7")  # 8
                oito = Label(text=listaVertices[7],
                           font="Verdana 7",
                           width=8).place(x=x[7] - 57, y=y[7])
            if maxV == 2:
                canvas.create_oval(x[8], y[8], x[8]+20, y[8]+20, fill="#0094e7")  # 9
                nove = Label(text=listaVertices[8],
                           font="Verdana 7",
                           width=8).place(x=x[8] + 22, y=y[8])
            if maxV == 1:
                canvas.create_oval(x[9], y[9], x[9]+20, y[9]+20, fill="#0094e7")  # 10
                dez = Label(text=listaVertices[9],
                           font="Verdana 7",
                           width=8).place(x=x[9] - 18, y=y[9] + 22)
            maxV = maxV - 1

    else:
        messagebox.showinfo("Alerta", "Lotado")

    vert.delete(0,"end")

def updatelist1():
    lig1["values"] = listaVertices
def updatelist2():
    lig2["values"] = listaVertices

def adicionaLigacao():
    for item1 in range(len(listaVertices)):
        for item2 in range(len(listaVertices)):
            if listaVertices[item1] == escolha1.get() and listaVertices[item2] == escolha2.get():
                if escolha1.get() == escolha2.get():
                    messagebox.showinfo("Alerta", "Laços não permitidos")
                else:
                    matrizLigacoes[item1][item2] += 1
                    matrizLigacoes[item2][item1] += 1
                    canvas.create_line(x[item1]+10,y[item1]+10,x[item2]+10,y[item2]+10)
                    if matrizLigacoes[item1][item2] > 1:
                        nA = Label(text = str(matrizLigacoes[item1][item2]),
                                   font = "Verdana 6 bold").place(x = (x[item1] + x[item2])/2, y = (y[item1] + y[item2])/2)
    print(matrizLigacoes)

def eule():
    cont1 = 0
    cont2 = 0
    soma = [0,0,0,0,0,0,0,0,0,0]

    for linha in range(len(listaVertices)):
        for coluna in range(len(listaVertices)):
            if matrizLigacoes[linha][coluna] > 0:
                cont1 += 1
                break
    print(cont1)

    for linha in range(len(listaVertices)):
        for coluna in range(len(listaVertices)):
            soma[linha] += matrizLigacoes[linha][coluna]

    for item in soma:
        if (item % 2) == 0 and item != 0:
            cont2 += 1
    print(cont2)

    if cont1 == len(listaVertices) and cont2 == len(listaVertices):
        resposta = Label(text = "Sim", font = "Verdana 8").place(x=165, y=472)
    else:
        resposta = Label(text="Não", font="Verdana 8").place(x=165, y=472)

def percurso(vertice):
    #
    grafoCopia1 = matrizLigacoes
    grafoCopia2 = matrizLigacoes

    prox = ""

    for item1 in range(len(listaVertices)):
        for item2 in tange(len(listaVertices)):
            if listaVertices[item1] == vertice:
                print(item1)
                if grafoCopia1[item1][item2] > 0:
                    print(item2)
                    prox = listaVertices[item2]





#------------------------------------------------
v = StringVar()
escolha1 = StringVar()
escolha2 = StringVar()

#Cria Canvas
canvas = Canvas(width = 400, height = 500)

#TITULO
titulo = Label(text = "PORTOS DO PARÁ",
               font = "Verdana 12 underline").place(x=125,y=5)

#ADICIONAR VETOR
vertLabel = Label(text = "Adicionar Vértice:",
                  font = "Verdana 10").place(x=10,y=50)
vert = Entry(width = 30, textvariable = v)
vert.place(x=140,y=52)
vertButton = Button(text = "OK",
                    font = "Verdana 10",
                    width = "5",
                    command = adicionaVertice)
vertButton.place(x=335,y=48)

#ADICIONAR LIGAÇÃO
lig1Label = Label(text = "Adicionar Ligação:",
                  font = "Verdana 10").place(x=10,y=90)
lig1 = ttk.Combobox(width = 15, postcommand = updatelist1, textvariable = escolha1)
lig1.place(x=140,y=91)
lig1Labele = Label(text = "e",
                  font = "Verdana 10").place(x=255,y=90)
lig2 = ttk.Combobox(width = 15, postcommand = updatelist2, textvariable = escolha2)
lig2.place(x=272,y=91)
ligButton = Button(text = "OK",
                   font = "Verdana 10",
                   width = "5",
                   command = adicionaLigacao)
ligButton.place(x=238,y=120)

#BOTÃO EULERIANO
euleButton = Button(text = "Verificar se é Euleriano",
                    font = "Verdana 8",
                    width = "20",
                    command = eule)
euleButton.place(x=10,y=470)

canvas.pack()
#-------------------------------------------------

root.mainloop()