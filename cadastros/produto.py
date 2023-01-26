import tkinter
import tkinter as TK
import requests
from tkcalendar import DateEntry
from tkinter import *
from tkinter import messagebox, ttk

#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Fabricantes::..")
#master.iconbitmap(default=" ")
master.geometry("580x620+400+00") #Largura x Altura + dist. Esquerda + dist. do topo

def buscador(event):
    # cep = '08490000'
    cep = txtCep.get()
    link = f"http://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(link)
    dicRequisicao = requisicao.json()

    estadobuscador = dicRequisicao['uf']
    logradourobuscador = dicRequisicao['logradouro']
    bairrobuscador = dicRequisicao['bairro']
    cidadebuscador = dicRequisicao['localidade']

    estado.set(estadobuscador)
    rua.set(logradourobuscador)
    bairro.set(bairrobuscador)
    cidade.set(cidadebuscador)
    txtnumero.focus_set()

def cancelarSair():
    resp = messagebox.askyesno("Cancelar e sair", 'Deseja realmente sair?')
    if resp == True:
        master.destroy()


#Nome
txtNome = Entry(master, bd=2, font=("Calibri, "), justify=LEFT)
txtNome.place(width=480, height=25, x=15, y=38)

#preço de Compra
txtPrecoCompra = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtPrecoCompra.place(width=150, height=25, x=15, y=88)

#preço de Venda
txtPrecoVenda = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtPrecoVenda.place(width=150, height=25, x=180, y=88)

#Peso
txtPeso = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtPeso.place(width=150, height=25, x=345, y=88)

#Data de Fabricação - #Calendário
lblDataFabricacao = Label(master,text= "Data de Fabricação:",font = "Calibri, 11").place(x=15, y=120)
datafabricacao = DateEntry(master, selectmode='year',font=("Calibri,12")).place(x=15,y=140, width=150,height=25)

#Data de Validade
lblDataValidade = Label(master,text= "Validade:",font = "Calibri, 11").place(x=180, y=120)
dataValidade = DateEntry(master, selectmode='year',font=("Calibri,12")).place(x=180,y=140, width=150,height=25)

#Data da cadastro
lblDataCadastro = Label(master,text= "Data de cadastro: ",font = "Calibri, 11").place(x=345, y=120)
dataCadastro= DateEntry(master, selectmode='year',font=("Calibri,12")).place(x=345, y=140, width=150,height=25)




#Fabricante
#label Fabricnate
lblFabricmate = Label(master,text= "Fabricante ",font = "Calibri, 11",).place(x=15, y=206)
# combo Fabricantes
campoSelect = TK.StringVar()
comboFabricante = ttk.Combobox(master, width=65, textvariable=(campoSelect))
comboFabricante.place(x=15, y=230)
comboFabricante['values'] = " "

#botão Adicionar Fabricante
btnAddFabricante = Button(master, text='+',font=("Calibri, 14"), command=" ")
btnAddFabricante.pack(side ='top')
btnAddFabricante.place(width=50, height=30, x=440, y=226)




#Label Cidade
lblFornecedor = Label(master,text= "Fornecedor: ",font = "Calibri, 11",).place(x=15, y=270)

#Fornecedor
# combo Fornecedor
campoSelect = TK.StringVar()
comboFornecedor = ttk.Combobox(master, width=65, textvariable=(campoSelect))
comboFornecedor.place(x=15, y=290)
comboFornecedor['values'] = " "

#botão Adicionar Fornecedor
btnAddFornecedor = Button(master, text='+',font=("Calibri, 14"), command=" ")
btnAddFornecedor.pack(side ='top')
btnAddFornecedor.place(width=50, height=30, x=440, y=290)


#Label Qauntidade
lblQuantidade = Label(master,text= "Quantidade: ",font = "Calibri, 11",).place(x=15, y=328)
#combo Quantidada
campoSelect = TK.StringVar()
comboQuantidade = ttk.Combobox(master, width=30, textvariable=(campoSelect))
comboQuantidade.place(x=15, y=348)
comboQuantidade['values'] = " "


#Label Valor Total
lblValorTotal = Label(master,text= "Valor Total: ",font = "Calibri, 11",).place(x=290, y=328)
#Valor Total
txtValorTotal = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtValorTotal.place(width=205, height=75, x=290, y=348)
#combo Quantidada
campoSelect = TK.StringVar()
comboQuantidade = ttk.Combobox(master, width=30, textvariable=(campoSelect))
comboQuantidade.place(x=15, y=348)
comboQuantidade['values'] = " "



#Label Forma de Pagamento
lblFormaPgto = Label(master,text= "Forma de pagamento: ",font = "Calibri, 11",).place(x=15, y=398)
#combo Forma de Pagamento
campoSelect = TK.StringVar()
comboFormaPgto = ttk.Combobox(master, width=30, textvariable=(campoSelect))
comboFormaPgto.place(x=15, y=418)
comboFormaPgto['values'] = " "
#botão Adicionar Fornecedor
btnAddFormaPgto = Button(master, text='+',font=("Calibri, 14"), command=" ")
btnAddFormaPgto.pack(side ='top')
btnAddFormaPgto.place(width=50, height=30, x=220, y=412)




#Observações
txtObservacao = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtObservacao.place(width=485, height=65, x=15, y=480)







#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=" ")
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=45, x=300, y=565)

#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command=cancelarSair)
btnCancelar.pack(side ='top')
btnCancelar.place(width=160, height=45, x=130, y=565)


#Label Endereco
lblNomeProduto = Label(master,text= "Nome do Produto: ",font = "Calibri, 11",).place(x=15, y=15)

#Label Peso
lblPeso = Label(master,text= "Peso: ",font = "Calibri, 11",).place(x=15, y=65)
#Label preco
lblPreco = Label(master,text= "Preço de compra: ",font = "Calibri, 11",).place(x=180, y=65)
#Label Cep
lblCep = Label(master,text= "Preço de Venda: ",font = "Calibri, 11",).place(x=345, y=65)






master.mainloop()