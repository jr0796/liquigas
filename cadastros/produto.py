import tkinter
import pyodbc
import tkinter as TK
from tkcalendar import DateEntry
from tkinter import *
from tkinter import messagebox, ttk


#Conexão com banco SQL

conexao = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T3K0RN5;PORT=1433;Database=bdLiquigas;Trusted_connection = yes')
print("Conexão bem sucedida!!")
cursor = conexao.cursor()



#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Fabricantes::..")
#master.iconbitmap(default=" ")
master.geometry("510x630+400+00") #Largura x Altura + dist. Esquerda + dist. do topo

sqlFabricante = "SELECT nomeFab FROM tbFabricante"
cursor.execute(sqlFabricante)
fabricantes = cursor.fetchall()

sqlFornecedor = "SELECT nomeForn FROM tbFornecedor"
cursor.execute(sqlFornecedor)
fornecedores = cursor.fetchall()

sqlFormaPgto = "SELECT descFormaPgtoProd FROM tbFormaPgtoProduto"
cursor.execute(sqlFormaPgto)
formasPgto = cursor.fetchall()


def cadastroProdutos():
    nomeProduto = txtNome.get()

    pesoProduto = txtPeso.get()
    precoCompra = txtPrecoCompra.get()
    precoVenda = txtPrecoVenda.get()

    dtaFabricacao = datafabricacao.get()
    dtaValidade = dataValidade.get()
    dtaDeCadastro = dataCadastro.get()

    quantidade = valorSelecionado.get()

    cmboFab = cmboFabricante.get()
    cmboForn = cmboPagamento.get()
    cmboPgto = cmboPagamento.get()

    observacoes = txtObservacao.get()


    #instrução SQL
    command = f"SELECT codFormaPgtoProd FROM tbFormaPgtoProduto WHERE descFormaPgtoProd =  '{cmboPgto}'"
    cursor.execute(command)
    pgto =(cursor.fetchall()[0])
    pgto = (int(pgto[0]))

    command = f"SELECT codFabricante FROM  tbFabricante WHERE nomeFab = '{cmboFab}'"
    cursor.execute(command)
    fab = (cursor.fetchall()[0])
    fab = (int(fab[0]))

    command = f"SELECT codFornecedor FROM tbFornecedor WHERE nomeForn = '{cmboForn}'"
    cursor.execute(command)
    dispo = (cursor.fetchall()[0])
    dispo = (int(dispo[0]))


    comando = f"""INSERT INTO tbProduto(nomeProduto,pesoProduto,precoCompraProduto,dataFabricacao,dataValidade,
                dataCadastro,quantidadeProduto,codFormaPgtoProduto)
                VALUES('{nomeProduto}','{pesoProduto}','{precoCompra}','{dtaFabricacao}','{dtaValidade}'
                ,'{dtaDeCadastro}','{quantidade}',{pgto},'{fab}','{dispo}')"""
    cursor.execute(comando)
    cursor.commit()



    #command = f""" INSERT INTO tbProduto(codFormaPgtoProduto)
     #       vALUES('{pgto}')"""
    #cursor.execute(command)
    #cursor.commit()






def cancelarSair():
    resp = messagebox.askyesno("Cancelar e sair", 'Deseja realmente sair?')
    if resp == True:
        master.destroy()

def novoFabricante( ):
    import fabricante

    fabricante
    #jan1.focus_set()  # Coloca o focu na janela aberta.
    #jan1.grab_set()  # desabilita a janela anterior

def novoFornecedor():
    import fornecedor
    fornecedor

def novaFormaPgto():
    import formaPgto
    formaPgto


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
datafabricacao = DateEntry(master, selectmode='year',font=("Calibri,12"),date_pattern='dd/mm/yyyy')
datafabricacao.place(x=15,y=140, width=150,height=25)

#Data de Validade
lblDataValidade = Label(master,text= "Validade:",font = "Calibri, 11").place(x=180, y=120)
dataValidade = DateEntry(master, selectmode='year',font=("Calibri,12"),date_pattern='dd/mm/yyyy')
dataValidade.place(x=180,y=140, width=150,height=25)

#Data da cadastro
lblDataCadastro = Label(master,text= "Data de cadastro: ",font = "Calibri, 11").place(x=345, y=120)
dataCadastro= DateEntry(master, selectmode='year',font=("Calibri,12"),date_pattern='dd/mm/yyyy')
dataCadastro.place(x=345, y=140, width=150,height=25)




#Fabricante
#label Fabricnate
lblFabricmate = Label(master,text= "Fabricante ",font = "Calibri, 11",).place(x=15, y=206)
# combo Fabricantes
cmboFabricante = TK.StringVar()
comboFabricante = ttk.Combobox(master, width=65, textvariable=(cmboFabricante))
comboFabricante.place(x=15, y=230)
#comboFabricante['values'] = " "

# Definir os valores do combo Fabricante
comboFabricante['values'] = [i[0] for i in fabricantes]

#botão Adicionar Fabricante
btnAddFabricante = Button(master, text='+',font=("Calibri, 14"), command=novoFabricante)
btnAddFabricante.pack(side ='top')
btnAddFabricante.place(width=50, height=30, x=440, y=226)




#Label Fornecedor
lblFornecedor = Label(master,text= "Fornecedor: ",font = "Calibri, 11",).place(x=15, y=270)

#Fornecedor
# combo Fornecedor
cmboFornecedor = TK.StringVar()
comboFornecedor = ttk.Combobox(master, width=65, textvariable=(cmboFornecedor))
comboFornecedor.place(x=15, y=290)
#comboFornecedor['values'] = " "
comboFornecedor['values'] = [j[0] for j in fornecedores]

#botão Adicionar Fornecedor
btnAddFornecedor = Button(master, text='+',font=("Calibri, 14"), command=novoFornecedor)
btnAddFornecedor.pack(side ='top')
btnAddFornecedor.place(width=50, height=30, x=440, y=290)

#Label Qauntidade
lblQuantidade = Label(master,text= "Quantidade: ",font = "Calibri, 11",).place(x=15, y=328)



#Label Valor Total
lblValorTotal = Label(master,text= "Valor Total: ",font = "Calibri, 11",).place(x=290, y=328)

#Valor Total
lblResult = Label(master,text= "R$ 0:00 ",font = "Calibri, 30",).place(x=290, y=348)
#lblResult.configure(text="R$ 0:00", text_color="green")


#Spinbox
valorSelecionado = tkinter.StringVar(value=1)
spinBox = ttk.Spinbox(master, from_=1,to=20,width=20, textvariable= valorSelecionado, wrap= True).place(x=15, y=348)


#Label Forma de Pagamento
lblFormaPgto = Label(master,text= "Forma de pagamento: ",font = "Calibri, 11",).place(x=15, y=398)
#combo Forma de Pagamento
cmboPagamento = TK.StringVar()
comboFormaPgto = ttk.Combobox(master, width=30, textvariable=(cmboPagamento))
comboFormaPgto.place(x=15, y=418)
#comboFormaPgto['values'] = " "
# Definir os valores do combo Forma de pagamento
comboFormaPgto['values'] = [jj[0] for jj in formasPgto]



#botão Adicionar Forma de pagamento
btnAddFormaPgto = Button(master, text='+',font=("Calibri, 14"), command=novaFormaPgto)
btnAddFormaPgto.pack(side ='top')
btnAddFormaPgto.place(width=50, height=30, x=220, y=412)




#Observações
txtObservacao = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtObservacao.place(width=485, height=65, x=15, y=480)







#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=cadastroProdutos)
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