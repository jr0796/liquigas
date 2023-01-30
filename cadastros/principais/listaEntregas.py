import tkinter as TK
from tkinter import *
from tkinter import ttk


#Construção da Janela
master = Tk()
master.title("..:: Confirmação de Entregas::..")
master.geometry("820x410+150+100") #Largura x Altura + dist. Esquerda + dist. topo

#Label
lblListaEntrega = Label(master, text="Lista de entregas:", font="Calibri, 11").place(x=10, y=10)

#TreeVew Lista de Espera
tv = ttk.Treeview(master, selectmode="browse", column=("Nº Venda", "Telefone", "Nome", "Endereco", "Bairro"),
                  show='headings', height=11)
tv.column("Nº Venda", width=70, minwidth=0, stretch=NO)
tv.heading("#1", text='Nº Venda')
tv.column("Telefone", minwidth=0, width=120, stretch=NO)
tv.heading("#2", text='Telefone')
tv.column("Nome", minwidth=0, width=200, stretch=NO)
tv.heading("#3", text='Nome')
tv.column("Endereco", minwidth=0, width=200, stretch=NO)
tv.heading("#4", text='Endereço')
tv.column("Bairro", minwidth=0, width=200, stretch=NO)
tv.heading("#5", text='Bairro')
tv.place(x=10, y=40)

#Label
lblListaEntrega = Label(master,text= "Situação : ",font = "Calibri, 11",).place(x=10, y=310)

#Combo Para confirmação
campoSelect = TK.StringVar()
comboConfirmacao = ttk.Combobox(master, width=52, textvariable=(campoSelect))
comboConfirmacao.place(x=10, y=330)
comboConfirmacao['values'] = " "

#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=" ")
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=55, x=645, y=310)
#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command="cancelarSair")
btnCancelar.pack(side ='top')
btnCancelar.place(width=160, height=55, x=470, y=310)

master.mainloop()