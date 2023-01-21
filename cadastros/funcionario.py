from tkinter import *
from tkinter import messagebox


#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Funcionários::..")
#master.iconbitmap(default=" ")
master.geometry("480x600+400+0") #Largura x Altura + dist. Esquerda + dist. direita

#Nome
txtNome = Entry(master, bd=2, font=("Calibri, "), justify=CENTER)
txtNome.place(width=440, height=25, x=15, y=38)

#RG
txtRg = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtRg.place(width=205, height=25, x=15, y=78)

#CPF
txtCpf = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtCpf.place(width=205, height=25, x=250, y=78)

#CEP
txtCep = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtCep.place(width=205, height=25, x=15, y=138)

#estado
txtEstado = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtEstado.place(width=205, height=25, x=250, y=138)

#rua
txtRua = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtRua.place(width=370, height=25, x=15, y=198)

#Número da rua
txtnumero = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtnumero.place(width=60, height=25, x=395, y=198)


#Bairro
txtBairro = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtBairro.place(width=205, height=25, x=15, y=258)

#Cidade
txtCidade = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtCidade.place(width=205, height=25, x=250, y=258)

#Complemento
txtComplemento = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtComplemento.place(width=205, height=25, x=15, y=318)


#Telefone
txtTelefone = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtTelefone.place(width=200, height=25, x=15, y=378)
#Caixa dos Telefones
txtCaixaTelefones = Entry(master, bd=2, font=("Calibri, 12"), justify=CENTER)
txtCaixaTelefones.place(width=205, height=75, x=15, y=418)

#Foto
txtFoto = Entry(master, bd=1, font=("Calibri, 12"), justify=CENTER)
txtFoto.place(width=110, height=115, x=350, y=348)
#botão Add Foto
btnAddFoto = Button(master, text='Add Foto',font=("Calibri, 12"), command="")
btnAddFoto.pack(side ='top')
btnAddFoto.place(width=110, height=25, x=350, y=466)


#botão Add Fone
btnAddFone = Button(master, text='+',font=("Calibri, 15"), command="")
btnAddFone.pack(side ='top')
btnAddFone.place(width=35, height=35, x=230, y=420)
#botão RM Fone
btnRmFone = Button(master, text='-',font=("Calibri, 15"), command="")
btnRmFone.pack(side ='top')
btnRmFone.place(width=35, height=35, x=230, y=460)


#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=" ")
btnConfirmar.pack(side ='top')
btnConfirmar.place(width=160, height=45, x=300, y=525)

#botão Cancelar
btnCancelar = Button(master, text='Cancelar', font=("Calibri, 12"), command="master")
btnCancelar.pack(side ='top')
btnCancelar.place(width=160, height=45, x=130, y=525)









master.mainloop()

