import requests
import tkinter
from tkinter import *
from tkinter import messagebox


#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Funcionários::..")
#master.iconbitmap(default=" ")
master.geometry("480x600+400+0") #Largura x Altura + dist. Esquerda + dist. direita


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


#Nome
txtNome = Entry(master, bd=2, font=("Calibri, "), justify=LEFT)
txtNome.place(width=440, height=25, x=15, y=38)

#RG
txtRg = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtRg.place(width=205, height=25, x=15, y=88)

#CPF
txtCpf = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtCpf.place(width=205, height=25, x=250, y=88)

#CEP
txtCep = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtCep.place(width=205, height=25, x=15, y=158)
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
txtBairro.place(width=205, height=25, x=15, y=278)

#Cidade
cidade = tkinter.StringVar()
txtCidade = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT,textvariable=cidade)
txtCidade.place(width=205, height=25, x=250, y=278)

#Complemento
txtComplemento = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtComplemento.place(width=205, height=25, x=15, y=338)


#Telefone
txtTelefone = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtTelefone.place(width=205, height=25, x=15, y=398)
#Caixa dos Telefones
txtCaixaTelefones = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT)
txtCaixaTelefones.place(width=205, height=75, x=15, y=438)

#Foto
txtFoto = Entry(master, bd=1, font=("Calibri, 12"), justify=LEFT)
txtFoto.place(width=110, height=115, x=345, y=372)
#botão Add Foto
btnAddFoto = Button(master, text='Add Foto',font=("Calibri, 12"), command="")
btnAddFoto.pack(side ='top')
btnAddFoto.place(width=110, height=25, x=345, y=490)


#botão Add Fone
btnAddFone = Button(master, text='+',font=("Calibri, 15"), command="")
btnAddFone.pack(side ='top')
btnAddFone.place(width=35, height=35, x=230, y=440)
#botão RM Fone
btnRmFone = Button(master, text='-',font=("Calibri, 15"), command="")
btnRmFone.pack(side ='top')
btnRmFone.place(width=35, height=35, x=230, y=480)


#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=" ")
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=45, x=300, y=545)

#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command="master")
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
lblCidade = Label(master,text= "Cidade: ",font = "Calibri, 11",).place(x=250, y=255)
#Label Complemento
lblComplemento = Label(master,text= "Complemento: ",font = "Calibri, 11",).place(x=15, y=315)
#Label Telefone
lblTelefone = Label(master,text= "Telefone: ",font = "Calibri, 11",).place(x=15, y=375)
#Label Foto
lblFoto = Label(master,text= "Foto: ",font = "Calibri, 11",).place(x=345, y=349)

master.mainloop()

