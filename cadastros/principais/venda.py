import tkinter as TK
from tkinter import *
from tkinter import ttk



from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Funcionários::..")
#master.iconbitmap(default=" ")
master.geometry("1100x750+100+0") #Largura x Altura + dist. Esquerda + dist. direita

#Top (data, hora, frase de boas vindas e destaques)###############
destaques = LabelFrame(master, text="Destaques", width= 1080, height=120)
destaques.place(x=1, y=1)

#Venda
lblVenda = Label(destaques,text= "Nº. Venda: ",font = "Calibri, 11",).place(x=1, y=1)
lblNumVenda = Label(destaques,text= "482 ",font = "Calibri, 11",).place(x=10, y=20)


#Label Atendente
lblAtendente = Label(destaques,text= "Atendente: ",font = "Calibri, 11",).place(x=1, y=45)
#Combo Atendente
campoSelect = TK.StringVar()
comboAtendente = ttk.Combobox(destaques, width=62, textvariable=(campoSelect))
comboAtendente.place(x=5, y=65)
comboAtendente['values'] = " "
#labelDiaSemana
lbldiaSemana = Label(destaques,text= "Segunda-Feira - 30/01/2023",font = "Calibri, 11",).place(x=800, y=1)
#LabelRelógio
lblrelogio = Label(destaques,text= "10:00 - Bom dia  - Usuário: Junior",font = "Calibri, 11",).place(x=850, y=70)


#Dados do cliente#################
dadosCliente = LabelFrame(master, text="Consulta de Clientes ", width= 1080, height=296)
dadosCliente.place(x=1, y=130)
#TelVEndedor
lblTelVendedor = Label(dadosCliente,text= "Telefone Cliente: ",font = "Calibri, 11",).place(x=1, y=1)
#txt Tel do Cliente
txtTelCliente = Entry(dadosCliente, bd=2, font=("Calibri, 12"), justify=LEFT)
txtTelCliente.place(width=200, height=20, x=1, y=25)
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




#Dados Produto########################
produtos = LabelFrame(master, text="Informações dos Produtos ", width= 1080, height=140)
produtos.place(x=1, y=420)
#Nome Produto
lblNomeProduto = Label(produtos,text= "Nome do Produto: ",font = "Calibri, 11",).place(x=1, y=1)
#Combo Produtos
campoSelect = TK.StringVar()
comboProdutos = ttk.Combobox(produtos, width=52, textvariable=(campoSelect))
comboProdutos.place(x=1, y=20)
comboProdutos['values'] = " "

#botão Add Produto à itens da venda
btnaddProdutoVenda = Button(produtos, text='+',font=("Calibri, 11"), command="")
btnaddProdutoVenda.pack(side ='top')
btnaddProdutoVenda.place(width=35, height=25, x=370, y=12)
#botão rm Produto à itens da venda
btnrmProdutoVenda = Button(produtos, text='-',font=("Calibri, 11"), command="")
btnrmProdutoVenda.pack(side ='top')
btnrmProdutoVenda.place(width=35, height=25, x=370, y=42)

#TreeVew Itens da Lista
tv = ttk.Treeview(produtos, selectmode="browse",column=("Produto","Valor","Qtde.","Sub-Total"),
                  show='headings', height=4,)
tv.column("Produto", width=270, minwidth=0, stretch=NO)
tv.heading("#1", text='Produto')
tv.column("Valor", minwidth=0,width=110,stretch=NO)
tv.heading("#2", text='Valor')
tv.column("Qtde.", minwidth=0,width=70,stretch=NO)
tv.heading("#3", text='Qtde.')
tv.column("Sub-Total", minwidth=0,width=150,stretch=NO)
tv.heading("#4", text='Sub-Total')
tv.place(x=440,y=5)

#Nome Valor do Produto
lblValorProduto = Label(produtos,text= "Valor do Produto: ",font = "Calibri, 11",).place(x=1, y=62)
lblPrecoProduto = Label(produtos,text= "R$: 10,00 ",font = "Calibri, 15",).place(x=1, y=80)

#Nome Valor do Produto
lblQtdeProduto = Label(produtos,text= "Quantidade: ",font = "Calibri, 11",).place(x=150, y=62)
#Spinbox Quantidade Produto
valorSelecionado = TK.StringVar(value=1)
spinBox = ttk.Spinbox(produtos, from_=1,to=20,width=5, textvariable= valorSelecionado, wrap= True).place(x=160, y=85)

#Nome Sub-total Item
lblsubTotalItem = Label(produtos,text= "Sub-total Item: ",font = "Calibri, 11",).place(x=260, y=62)
lblsubTotalItem = Label(produtos,text= "R$: 30,00 ",font = "Calibri, 15",).place(x=260, y=85)


#Valores#######################
valores = LabelFrame(master, text="Valores da Venda", width= 500, height=120)
valores.place(x=1,y=565)

#Label Total
lblTotal = Label(valores,text= "Total: ",font = "Calibri, 11",).place(x=1, y=1)
lblTotalResult = Label(valores,text= "R$: 200,00",font = "Calibri, 15",).place(x=1, y=20)

#Label Valor REcebido
lblRecebido = Label(valores,text= "Valor Recebido: ",font = "Calibri, 11",).place(x=180, y=1)
#Valor Recebido
txtRecebido= Entry(valores, bd=2, font=("Calibri, 15"), justify=LEFT)
txtRecebido.place(width=120, height=25, x=170, y=20)
#lbl Troco
lblTroco = Label(valores,text= "Troco: ",font = "Calibri, 11",).place(x=390, y=1)
lblResulTroco= Label(valores,text= "R$ 100,00 ",font = "Calibri, 15",).place(x=390, y=20)
#Combo Forma de pagamento
campoSelect = TK.StringVar()
comboFormaPgto = ttk.Combobox(valores, width=62, textvariable=(campoSelect))
comboFormaPgto.place(x=1, y=50)
comboFormaPgto['values'] = " "
#Radio Entraga
#radioselected = Tk.StringVar()
radio1 = ttk.Radiobutton(valores,text="Com entrega", value="Value1")
radio1.place(x=300, y=80)
radio2 = ttk.Radiobutton(valores,text="Sem entrega", value="Value2")
radio2.place(x=400, y=80)


#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=" ")
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=45, x=900, y=565)
#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command="cancelarSair")
btnCancelar.pack(side ='top')
btnCancelar.place(width=160, height=45, x=750, y=565)
#botão Limpar
btnLimpar = Button(master, text='Cancelar', font=("Calibri, 12"), command="cancelarSair")
btnLimpar.pack(side ='top')
btnLimpar.place(width=160, height=45, x=620, y=565)


master.mainloop()