from tkcalendar import Calendar
from tkcalendar import DateEntry
import requests
import tkinter as TK
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Veículos::..")
#master.iconbitmap(default=" ")
master.geometry("510x600+400+0") #Largura x Altura + dist. Esquerda + dist. direita




def cancelarSair():
    resp = messagebox.askyesno("Cancelar e sair", 'Deseja realmente sair?')
    if resp == True:
        master.destroy()


oframe = Frame(master,width=490, height= 260,bg="white" ).place(x=10,y=20)

#Label Nome do Veículo ou Identificação
lblNomeVeic = Label(master,text= "Nome do veículo: ",font = "Calibri, 11",bg="white").place(x=15, y=35)
#Nome do Veículo ou Identificação
txtNome = Entry(master, bd=2, font=("Calibri,12 "), justify=LEFT)
txtNome.place(width=455, height=25, x=15, y=55)


#Label Nome do proprietário
lblNomeProprietario = Label(master,text= "Proprietário: ",font = "Calibri, 11",bg="white").place(x=15, y=90)
# combo Proprietário
campoSelect = TK.StringVar()
#master = novaMidia
comboProprietario = ttk.Combobox(master, width=62, textvariable=(campoSelect))
comboProprietario.place(x=20, y=110)
comboProprietario['values'] = " "
#comboProprietario.current(0)
#botão Confirmar
btnAddProprietario = Button(master, text='+',font=("Calibri, 14"), command=" ")
btnAddProprietario.pack(side ='top')
btnAddProprietario.place(width=50, height=30, x=420, y=105)

#Label Nome do Fabricante
lblFabricante = Label(master,text= "Fabricante: ",font = "Calibri, 11",bg="white").place(x=20, y=140)
# combo Fabricante ou montadora
campoSelect = TK.StringVar()
comboMontadora = ttk.Combobox(master, width=30, textvariable=(campoSelect))
comboMontadora.place(x=20, y=160)
comboMontadora['values'] = " "
#comboMontadora.current(0)

#botão Add Montadora
btnaddMontadora = Button(master, text='+',font=("Calibri, 12"), command=" ")
btnaddMontadora.pack(side ='top')
btnaddMontadora.place(width=30, height=30, x=230, y=155)


#Label Nome do Fabricante
lblModelo = Label(master,text= "Modelo: ",font = "Calibri, 11",bg="white").place(x=300, y=140)
# combo Modelo
campoSelect = TK.StringVar()
comboModelo = ttk.Combobox(master, width=20, textvariable=(campoSelect))
comboModelo.place(x=290, y=160)
comboModelo['values'] = " "
#comboModelo.current(0)
#botão Add Montadora
btnaddMontadora = Button(master, text='+',font=("Calibri, 12"), command=" ")
btnaddMontadora.pack(side ='top')
btnaddMontadora.place(width=30, height=30, x=440, y=155)


#Label Nome do Fabricante
lblCor = Label(master,text= "Cor: ",font = "Calibri, 11",bg="white").place(x=20, y=200)
# combo Cor
campoSelect = TK.StringVar()
comboCor = ttk.Combobox(master, width=30, textvariable=(campoSelect))
comboCor.place(x=20, y=220)
comboCor['values'] = " "
#comboCor.current(0)
#btn add Cor
btnaddCor = Button(master, text='+',font=("Calibri, 12"), command=" ")
btnaddCor.pack(side ='top')
btnaddCor.place(width=30, height=30, x=230, y=216)

# combo Tipo de Combustível
campoSelect = TK.StringVar()
comboCombustivel = ttk.Combobox(master, width=20, textvariable=(campoSelect))
comboCombustivel.place(x=290, y=223)
comboCombustivel['values'] = " "
#comboCombustivel.current(0)
#btn add Cor
btnaddCombustivel = Button(master, text='+',font=("Calibri, 12"), command=" ")
btnaddCombustivel.pack(side ='top')
btnaddCombustivel.place(width=30, height=30, x=440, y=216)
lblcombustivel = Label(master,text= "Combustível: ",font = "Calibri, 11",bg="white").place(x=290, y=200)


lblkm = Label(master,text= "Quilometragem: ",font = "Calibri, 11").place(x=20, y=290)
#Quilometragem
txtQuilometragem = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtQuilometragem.place(width=205, height=25, x=20, y=310)

#Ano de fabricação
lblkm = Label(master,text= "Ano de Fabricação:",font = "Calibri, 11").place(x=290, y=290)
txtAnoFabri = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtAnoFabri.place(width=150, height=25, x=290, y=310)

#Data de Registro
lblDataRegistro  = Label(master,text= "Data de Registro:",font = "Calibri, 11").place(x=290, y=340)
#Calendário
#cal = Calendar(master, selectmode='day', year=2020, month=5, day=22).place(x=250, y=308,width=90, height=100)
anoFabri = DateEntry(master, selectmode='year',font=("Calibri,12")).place(x=290,y=360, width=150,height=25)


lblPlaca = Label(master,text= "Placa:",font = "Calibri, 11").place(x=20, y=340)
#Quilometragem
txtPlaca = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtPlaca.place(width=205, height=25, x=20, y=360)

lblRenavan = Label(master,text= "Renavan:",font = "Calibri, 11").place(x=20, y=390)
#Quilometragem
txtRenavan = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtRenavan.place(width=205, height=25, x=20, y=410)

#Forma de pagamento
lblFormadePgto = Label(master,text= "Forma de Pagamento:",font = "Calibri, 11").place(x=20, y=450)
# combo Tipo de Combustível
campoSelect = TK.StringVar()
comboFormaPgto = ttk.Combobox(master, width=30, textvariable=(campoSelect))
comboFormaPgto.place(x=20, y=470)
comboFormaPgto['values'] = " "
#comboCombustivel.current(0)


#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=" ")
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=45, x=300, y=545)

#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command=cancelarSair)
btnCancelar.pack(side ='top')
btnCancelar.place(width=160, height=45, x=130, y=545)





master.mainloop()
