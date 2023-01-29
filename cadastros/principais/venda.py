import tkinter as TK
from tkinter import *
from tkinter import ttk


from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Funcionários::..")
#master.iconbitmap(default=" ")
master.geometry("1100x650+100+0") #Largura x Altura + dist. Esquerda + dist. direita

#Top (data, hora, frase de boas vindas e destaques)
destaques = LabelFrame(master, text="Destaques", width= 1080, height=140)
destaques.pack( expand="No")
destaques.grid_propagate(0)

#Venda
lblVenda = Label(destaques,text= "Nº. Venda: ",font = "Calibri, 11",).place(x=1, y=1)
#Caixa com número das vendas
txtnumVenda = Entry(destaques, bd=2, font=("Calibri, 12"), justify=LEFT)
txtnumVenda.place(width=100, height=25, x=1, y=25)

#Label Atendente
lblAtendente = Label(destaques,text= "Atendente: ",font = "Calibri, 11",).place(x=1, y=55)
#Combo Atendente
campoSelect = TK.StringVar()
comboAtendente = ttk.Combobox(master, width=62, textvariable=(campoSelect))
comboAtendente.place(x=12, y=95)
comboAtendente['values'] = " "
#labelDiaSemana
lbldiaSemana = Label(destaques,text= "Segunda-Feira - 30/01/2023",font = "Calibri, 11",).place(x=800, y=1)
#LabelRelógio
lblrelogio = Label(destaques,text= "10:00 - Bom dia  - Usuário: Junior",font = "Calibri, 11",).place(x=850, y=90)


#Dados do cliente
dadosCliente = LabelFrame(master, text="Consulta de Clientes ", width= 1080, height=296)
dadosCliente.pack(expand="yes")
#TelVEndedor
lblTelVendedor = Label(dadosCliente,text= "Telefone Cliente: ",font = "Calibri, 11",).place(x=1, y=1)
#txt Tel do Cliente
txtTelCliente = Entry(dadosCliente, bd=2, font=("Calibri, 12"), justify=LEFT)
txtTelCliente.place(width=200, height=25, x=1, y=25)
#botão Pesquisar Fone
btnPesquisarFone = Button(dadosCliente, text='Consultar',font=("Calibri, 11"), command="")
btnPesquisarFone.pack(side ='top')
btnPesquisarFone.place(width=45, height=35, x=220, y=20)
#Nome do Cliente
lblNomeCliente = Label(dadosCliente,text= "Nome: ",font = "Calibri, 11").place(x=1, y=55)
#TXT Nome do Cliente
txtNomeCliente = Entry(dadosCliente, bd=2, font=("Calibri, 12"), justify=LEFT)
txtNomeCliente.place(width=430, height=25, x=1, y=75)
#endereco
lblEnderecoCliente= Label(dadosCliente,text= "Rua: ",font = "Calibri, 11",).place(x=1, y=110)
#TXT Endereco
txtEnderecoCliente= Entry(dadosCliente, bd=2, font=("Calibri, 12"), justify=LEFT)
txtEnderecoCliente.place(width=200, height=25, x=1, y=130)
#lbl Bairro
lblBairro = Label(dadosCliente,text= "Bairro: ",font = "Calibri, 11",).place(x=230, y=110)
#Caixa com número das vendas
txtBairro = Entry(dadosCliente, bd=2, font=("Calibri, 12"), justify=LEFT)
txtBairro.place(width=200, height=25, x=230, y=130)
#Observações
lblObservacoes = Label(dadosCliente,text= "Observações: ",font = "Calibri, 11",).place(x=1, y=170)
#Caixa com número das vendas
txtobservacoes= Entry(dadosCliente, bd=2, font=("Calibri, 12"), justify=LEFT)
txtobservacoes.place(width=430, height=79, x=1, y=190)
#TreeVew REsultado da consulta
tv = ttk.Treeview(dadosCliente, selectmode="browse",column=("Telefone","Nome","Endereco","Bairro","Observacoes"),
                  show='headings',height=11)
tv.column("Telefone", width=50, minwidth=0, stretch=NO)
tv.heading("#1", text='Telefone')
tv.column("Nome", minwidth=0,width=250,stretch=NO)
tv.heading("#2", text='Nome')
tv.column("Endereco", minwidth=0,width=100,stretch=NO)
tv.heading("#3", text='Endereço')
tv.column("Bairro", minwidth=0,width=100,stretch=NO)
tv.heading("#4", text='Bairro')
tv.column("Observacoes", minwidth=0,width=100,stretch=NO)
tv.heading("#5", text='Observações')
tv.place(x=440,y=22)




#Dados Produto
produtos = LabelFrame(master, text="Informações dos Produtos ", width= 1080, height=120)
produtos.pack(expand=1)

#Valores
valores = LabelFrame(master, text="Valores da Venda", width= 1080, height=120)
valores.pack(expand="no", anchor='n')





master.mainloop()