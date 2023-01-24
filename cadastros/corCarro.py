
import tkinter
from tkinter import *
from tkinter import messagebox


#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Cores::..")
#master.iconbitmap(default=" ")
master.geometry("480x280+400+0") #Largura x Altura + dist. Esquerda + dist. direita

lblTitulo = Label(master,text= "Cadastro de Cores ",font = "Calibri, 20",).place(x=140, y=5)


#Label Nome
lblNome = Label(master,text= "Nome: ",font = "Calibri, 11",).place(x=25, y=55)
#TXT Nome
txtNome = Entry(master, bd=2, font=("Calibri, 12 "), justify=LEFT)
txtNome.place(width=440, height=25, x=25, y=78)


#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=" ")
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=45, x=300, y=200)

#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command="")
btnCancelar.pack(side ='top')
btnCancelar.place(width=160, height=45, x=130, y=200)






master.mainloop()