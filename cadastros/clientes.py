import re
import requests
import pyodbc
import tkinter
from tkinter import *
from tkinter import messagebox


from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


#Conexão com banco SQL
conexao = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T3K0RN5;PORT=1433;Database=bdLiquigas;Trusted_connection = yes')
print("Conexão bem sucedida!!")
cursor = conexao.cursor()





#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Clientes::..")
#master.iconbitmap(default=" ")
master.geometry("480x600+400+0") #Largura x Altura + dist. Esquerda + dist. direita


def buscador(event):
    # cep = '08490000'
    try:
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
        #Vídeo com exemplo do uso de eventos
        #documentação com os principais eventos: https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
    except:
        messagebox.showinfo("Erro!", "Verifique a conexão com a internet \n ou digite um CEP válido." )
        txtCep.configure(validatecommand=(numCEPcmd, '%S'))
        txtCep.delete(0, "end")
        txtCep.configure(validatecommand=(numCEPcmd, '%P'))
        txtCep.focus_set()

def limparCampos():

    txtRg.configure(validatecommand=(numRgcmd, '%S'))
    txtRg.delete(0, "end")

    txtNome.delete(0, "end")

    txtCpf.configure(validatecommand=(numCpfcmd, '%S'))
    txtCpf.delete(0, "end")

    txtRua.delete(0, "end")

    txtCep.configure(validatecommand=(numCEPcmd, '%S'))
    txtCep.delete(0, "end")

    txtCidade.delete(0, "end")
    txtBairro.delete(0, "end")
    txtnumero.delete(0, "end")
    txtEstado.delete(0, "end")
    txtComplemento.delete(0, "end")

    txtTelefone.configure(validatecommand=(numeriCmd, "%S"))
    txtTelefone.delete(0, END)
    txtCaixaTelefones.configure(state="normal")  # habilidanto lista
    txtCaixaTelefones.delete("1.0", "end")  # Limpando caixa

def cancelarSair():
    resp = messagebox.askyesno("Cancelar e sair", 'Deseja realmente sair?')
    if resp == True:
        master.destroy()

def cadastrarCli():
    nomeCli = txtNome.get()
    rgCli = txtRg.get()
    cpfCli = txtCpf.get()
    cepCli =txtCep.get()
    ufCli = txtEstado.get()
    logrCli = txtRua.get()
    numLogrCli = txtnumero.get()
    bairroCli = txtBairro.get()
    cidadeCli = txtCidade.get()
    compCLi = txtComplemento.get()

    foneCli = txtCaixaTelefones.get("1.0", "end").splitlines()


    limparCampos()
    messagebox.showinfo("Cadastro", "Dados cadastrados com Sucesso!")
    txtNome.focus_set()


#instruções SQL
    commando = f""" INSERT INTO tbCliente(nomeCliente,rgCliente,cpfCliente,cepCliente,ufCliente,
    logrCliente,numLogrCliente,bairroCliente,cidadeCliente,compCliente)
    VALUES ('{nomeCli}','{rgCli}','{cpfCli}','{cepCli}','{ufCli}','{logrCli}','{numLogrCli}','{bairroCli}','{cidadeCli}'
    ,'{compCLi}')"""
    # executando:
    cursor.execute(commando)
    cursor.commit()


    commando = f"SELECT codCliente FROM tbCliente WHERE nomeCliente = '{nomeCli}' "
    #executando:
    cursor.execute(commando)
    result = cursor.fetchall()[0]
    result2 = result


    for i, item in enumerate(foneCli):
        if item == "":
            print()
        else:
            commando = f"""INSERT INTO tbTelCliente(numTelCliente, codCliente) VALUES ('{item}' , {result2[0]})"""
            cursor.execute(commando)
            cursor.commit()
            print(item)

#Lista de telefones
def maisFone():

    num_linhas = int(txtCaixaTelefones.index('end-1c').split('.')[0])

    if num_linhas < 5:
        txtCaixaTelefones.configure(state="normal")
        txtCaixaTelefones.insert('end', f'{txtTelefone.get()}\n')
        txtCaixaTelefones.configure(state="disabled")
        txtTelefone.focus_set()
    else:
        txtTelefone.delete(0, "end")
        txtCaixaTelefones.focus_set()
        messagebox.showinfo("Atenção", "Você atingiu o número máximo de telefones cadastrados!")

    txtTelefone.configure(validatecommand=(numeriCmd, "%S"))
    txtTelefone.delete(0, END)
    txtTelefone.focus_set()
    txtTelefone.configure(validatecommand=(numeriCmd, "%P"))
def menosFone():
    selecao = txtCaixaTelefones.tag_ranges("sel") #identificando linha selcionada
    txtCaixaTelefones.configure(state="normal") #habilidanto lista
    i = txtCaixaTelefones.index(selecao[0]) # índice do parametro "sel"
    ii =txtCaixaTelefones.index(selecao[1]) # índice do parametro "se"
    linha_selecionada = int(i.split(".")[0])-1 #recuperando índice
    linhas = txtCaixaTelefones.get("1.0", "end").splitlines() #contando linhas
    linhas.pop(linha_selecionada) #apagando linha selecionada
    novaLista = "".join(linhas) #removendo linhas em branco, juntando lista novamente
    txtCaixaTelefones.delete("1.0", "end") #Limpando caixa
    txtCaixaTelefones.insert(END, novaLista) #recarregando a nova lista
    #desabilitando edição da lista
    txtCaixaTelefones.configure(state="disable")  # habilidanto lista


#Validações

#Telefone
def textNumerico(text):

    if text.isdigit() and len(text) < 12:
        return True
    else:
        return False
numeriCmd = master.register(textNumerico)

def valorRg(text):
    if text.isdigit() and len(text) < 10:
        return True
    else:
        return False
numRgcmd = master.register(valorRg)

def valorCpf(text):
    if text.isdigit() and len(text) < 12:
        return True
    else:
        return False
numCpfcmd = master.register(valorCpf)

def valorCEP(text):
    if text.isdigit() and len(text) < 9:
        return True
    else:
        return False
numCEPcmd = master.register(valorCEP)
#=========================================


#Nome
txtNome = Entry(master, bd=2, font=("Calibri, "), justify=LEFT)
txtNome.place(width=440, height=25, x=15, y=38)

#RG
txtRg = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT, validate="key" )
txtRg.place(width=205, height=25, x=15, y=88)
txtRg.configure(validatecommand=(numRgcmd, '%P'))

#CPF
txtCpf = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT, validate="key")
txtCpf.place(width=205, height=25, x=250, y=88)
txtCpf.configure(validatecommand=(numCpfcmd, '%P'))

#CEP
txtCep = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT, validate="key")
txtCep.place(width=205, height=25, x=15, y=158)
txtCep.configure(validatecommand=(numCEPcmd,'%P'))
txtCep.bind("<FocusOut>", buscador)

#estado
estado = tkinter.StringVar()
txtEstado = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT,textvariable=estado)
txtEstado.place(width=205, height=25, x=250, y=158)

#rua
rua = tkinter.StringVar()
txtRua = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT,textvariable=rua)
txtRua.place(width=370, height=25, x=15, y=218)

#Número da rua
txtnumero = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtnumero.place(width=60, height=25, x=395, y=218)

#Bairro
bairro = tkinter.StringVar()
txtBairro = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT,textvariable=bairro)
txtBairro.place(width=285, height=25, x=15, y=278)

#Cidade
cidade = tkinter.StringVar()
txtCidade = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT,textvariable=cidade)
txtCidade.place(width=150, height=25, x=306, y=278)

#Complemento
txtComplemento = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtComplemento.place(width=205, height=25, x=15, y=338)

#Telefone
txtTelefone = Entry(master, bd=2, font=("Calibri, 12"), validate="key", justify=LEFT)
txtTelefone.place(width=205, height=25, x=15, y=398)
txtTelefone.configure(validatecommand=(numeriCmd, '%P'))

#Caixa de texto para os telefones
txtCaixaTelefones = Text(master, bd=2, font=("Calibri, 12"),state="disable")
txtCaixaTelefones.place(width=205, height=75, x=15, y=438)

#botão Add Fone
btnAddFone = Button(master, text='+', font=("Calibri, 15"), command= maisFone)
btnAddFone.pack(side ='top')
btnAddFone.place(width=35, height=35, x=230, y=440)
#botão RM Fone'
btnRmFone = Button(master, text='-',font=("Calibri, 15"), command=menosFone)
btnRmFone.pack(side ='top')
btnRmFone.place(width=35, height=35, x=230, y=480)


#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=cadastrarCli)
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=45, x=300, y=545)

#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command=cancelarSair)
btnCancelar.pack(side ='top')
btnCancelar.place(width=160, height=45, x=130, y=545)

#Label Endereco
lblTelefone = Label(master,text= "Nome: ",font = "Calibri, 11",).place(x=15, y=15)

#Label RG
lblRg = Label(master,text= "RG: ",font = "Calibri, 11",).place(x=15, y=65)
#Label CPF
lblCpf = Label(master,text= "CPF: ",font = "Calibri, 11",).place(x=250, y=65)
#Label Cep
lblCep = Label(master,text= "CEP: ",font = "Calibri, 11",).place(x=15, y=135)
#Label Estado
lblEstado = Label(master,text= "Estado: ",font = "Calibri, 11",).place(x=250, y=135)
#Label Rua
lblRua = Label(master,text= "Logradouro: ",font = "Calibri, 11",).place(x=15, y=195)
#Label Número
lblNum = Label(master,text= "Nº: ",font = "Calibri, 11",).place(x=395, y=195)
#Label Bairro
lblBairro = Label(master,text= "Bairro: ",font = "Calibri, 11",).place(x=15, y=255)
#Label Cidade
lblCidade = Label(master,text= "Cidade: ",font = "Calibri, 11",).place(x=306, y=255)
#Label Complemento
lblComplemento = Label(master,text= "Complemento: ",font = "Calibri, 11",).place(x=15, y=315)
#Label Telefone
lblTelefone = Label(master,text= "Telefone: ",font = "Calibri, 11",).place(x=15, y=375)


master.mainloop()

