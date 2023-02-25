

import pyodbc
import requests
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from  datetime import date




#Conexão com banco SQL
conexao = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T3K0RN5;PORT=1433;Database=bdLiquigas;Trusted_connection = yes')
print("Conexão bem sucedida!!")
cursor = conexao.cursor()


#Construção da Janela
master = Tk()
master.title("..:: Cadastro de Funcionários::..")
#master.iconbitmap(default=" ")
master.geometry("480x600+400+0") #Largura x Altura + dist. Esquerda + dist. direita

fotodoFunc = ("C:/Users/anton/Pictures/avatar.png")



def buscador(event):
    try:
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
        #Vídeo com exemplo do uso de eventos
        #documentação com os principais eventos: https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
    except:
        messagebox.showinfo("Erro!", "Verifique a conexão com a internet \n ou digite um CEP válido.")

def cancelarSair():
    resp = messagebox.askyesno("Cancelar e sair", 'Deseja realmente sair?')
    if resp == True:
        master.destroy()

def addFoto():
    filename = filedialog.askopenfilename()  # Isto te permite selecionar um arquivo

    global fotoTK, arquivoFunc
    with open (filename, 'rb') as foto:
        armazenbyte = foto.read()
        arquivoFunc = armazenbyte

    caminhoImagem = filename
    imagine = Image.open(caminhoImagem)
    fotoTK = ImageTk.PhotoImage(imagine)
    lblFoto = Label(master, image=fotoTK, width=110, height=115).place(x=345, y=372)

def limparCampo():
    txtNome.delete(0, "end")

    txtRg.configure(validatecommand=(validRg, '%S'))
    txtRg.delete(0, "end")

    txtCpf.configure(validatecommand=(validCpf, '%S'))
    txtCpf.delete(0, "end")

    txtCep.configure(validatecommand=(validCep, '%S'))
    txtCep.delete(0, "end")

    txtEstado.delete(0, "end")
    txtRua.delete(0, "end")
    txtnumero.delete(0, "end")
    txtBairro.delete(0, "end")
    txtCidade.delete(0, "end")
    txtComplemento.delete(0, "end")
    txtNome.focus_set()

    txtRg.configure(validatecommand=(validRg, '%P'))
    txtCpf.configure(validatecommand=(validCpf, '%P'))
    txtCep.configure(validatecommand=(validCep, '%P'))


    #caminhoImagem = ("C:/Users/anton/Pictures/avatar.png")
    imagine = Image.open("C:/Users/anton/Pictures/avatar.png")
    fotolimpa = ImageTk.PhotoImage(imagine)
    lblFoto = Label(master, image=fotolimpa, width=110, height=115).place(x=345, y=372)
    #lblFoto = Label(master, image=fotodoFunc, width=110, height=115).place(x=345, y=372)

    #dataAgora = datetime.datetime.now().date()
    hoje = date.today()
    #dtaContratacao.configure(day=dataAgora.day,month=dataAgora.month,year=dataAgora.year)
    dtaContratacao.set_date(hoje)

    txtCaixaTelefones.configure(state="normal")  # habilidanto lista
    txtCaixaTelefones.delete("1.0", "end")  # Limpando caixa

def cadastroFunc():
    nomefunc = txtNome.get()
    rgFunc  = txtRg.get()
    cpfFunc = txtCpf.get()
    cepFunc = txtCep.get()
    ufFunc  = txtEstado.get()
    logrFunc = txtRua.get()
    numLogrFunc = txtnumero.get()
    bairroFunc = txtBairro.get()
    cidadeFunc = txtCidade.get()
    compleFunc = txtComplemento.get()
    paisFunc = ("Brasil")

    #foneFunc = txtTelefone.get()
    foneFunc = txtCaixaTelefones.get("1.0","end").splitlines()

    dataContratacao = dtaContratacao.get()
    fotoFunc = pyodbc.Binary(arquivoFunc)






    #instrução SQL
    command = f"""INSERT INTO tbFuncionario(nomeFunc, rgFunc,cpfFunc, logrFunc, numLogrFunc,cepFunc,bairroFunc, 
            cidadeFunc, ufFunc,compFunc,paisFunc,dataContratacao, fotoFunc)
            SELECT '{nomefunc}','{rgFunc}','{cpfFunc}','{logrFunc}','{numLogrFunc}','{cepFunc}','{bairroFunc}','{cidadeFunc}',
            '{ufFunc}','{compleFunc}','{paisFunc}', '{dataContratacao}', BULKColumn
            FROM OPENROWSET (BULK 'C:/Users/anton/Pictures/capa.jpg' , SINGLE_BLOB) AS FotoDoFunc """

    cursor.execute(command)
    cursor.commit()

    commando = f"SELECT codFunc FROM tbFuncionario WHERE nomeFunc = '{nomefunc}' "
    # executando:
    cursor.execute(commando)
    result = cursor.fetchall()[0]
    result2 = result

    for i, item in enumerate(foneFunc):
        if item == "":
            print()
        else:
            commando = f"""INSERT INTO tbTelFuncinoario(numTelFunc, codFunc) VALUES ('{item}' , {result2[0]})"""
            cursor.execute(commando)
            cursor.commit()
            print(item)


    # limparCampos()
    messagebox.showinfo("Cadastro", "Dados cadastrados com sucesso.")
    txtNome.focus_set()
    print(fotoFunc)
    print(dataContratacao)
    limparCampo()

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

    txtTelefone.configure(validatecommand=(validTel, "%S"))
    txtTelefone.delete(0, END)
    txtTelefone.focus_set()
    txtTelefone.configure(validatecommand=(validTel, "%P"))
def menosFone():
    selecao = txtCaixaTelefones.tag_ranges("sel")  # identificando linha selcionada
    txtCaixaTelefones.configure(state="normal")  # habilidanto lista
    i = txtCaixaTelefones.index(selecao[0])  # índice do parametro "sel"
    ii = txtCaixaTelefones.index(selecao[1])  # índice do parametro "se"
    linha_selecionada = int(i.split(".")[0]) - 1  # recuperando índice
    linhas = txtCaixaTelefones.get("1.0", "end").splitlines()  # contando linhas
    linhas.pop(linha_selecionada)  # apagando linha selecionada
    novaLista = "".join(linhas)  # removendo linhas em branco, juntando lista novamente
    txtCaixaTelefones.delete("1.0", "end")  # Limpando caixa
    txtCaixaTelefones.insert(END, novaLista)  # recarregando a nova lista
    # desabilitando edição da lista
    txtCaixaTelefones.configure(state="disable")  # habilidanto lista


#Validações
#===========================

def limiteTel(text):
    if text.isdigit() and len(text) < 12:
        return True
    else:
        return False
validTel = master.register(limiteTel)

def limiteRg(text):
    if text.isdigit() and len(text) < 10:
        return True
    else:
        return False
validRg = master.register(limiteRg)

def limiteCpf(text):
    if text.isdigit() and len(text) < 12:
        return True
    else:
        return False
validCpf = master.register(limiteCpf)

def limitCep(text):
    if text.isdigit() and len(text) < 9:
        return True
    else:
        return False
validCep = master.register(limitCep)



#Nome
txtNome = Entry(master, bd=2, font=("Calibri, "), justify=LEFT)
txtNome.place(width=440, height=25, x=15, y=38)

#RG
txtRg = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT, validate="key")
txtRg.place(width=205, height=25, x=15, y=88)
txtRg.configure(validatecommand=(validRg, '%P'))

#CPF
txtCpf = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT, validate="key")
txtCpf.place(width=205, height=25, x=250, y=88)
txtCpf.configure(validatecommand=(validCpf, '%P'))

#CEP
txtCep = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT, validate="key")
txtCep.place(width=205, height=25, x=15, y=158)
txtCep.bind("<FocusOut>", buscador)
txtCep.configure(validatecommand=(validCep, '%P'))

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
txtTelefone = Entry(master, bd=2, font=("Calibri, 12"), justify=LEFT, validate="key")
txtTelefone.place(width=205, height=25, x=15, y=398)
txtTelefone.configure(validatecommand=(validTel, '%P'))

#Caixa dos Telefones
txtCaixaTelefones = Text(master, bd=2, font=("Calibri, 12"), state="disable")
txtCaixaTelefones.place(width=205, height=75, x=15, y=438)

#Data de contrataçõa
dtaContratacao = DateEntry(master, width=20, background='darkblue', foreground='white', borderwidth=2,date_pattern='dd/mm/yyyy')
dtaContratacao.place(x=300,y=340)

#Foto
caminhoPadrao = Image.open(fotodoFunc)
fotoPadrao = ImageTk.PhotoImage(caminhoPadrao)
lblFoto = Label(master, image=fotoPadrao,width=110, height=115).place(x=345, y=372)



#botão Add Foto
btnAddFoto = Button(master, text='Add Foto',font=("Calibri, 12"), command=addFoto)
btnAddFoto.pack(side ='top')
btnAddFoto.place(width=110, height=25, x=345, y=490)


#botão Add Fone
btnAddFone = Button(master, text='+',font=("Calibri, 15"), command=maisFone)
btnAddFone.pack(side ='top')
btnAddFone.place(width=35, height=35, x=230, y=440)
#botão RM Fone
btnRmFone = Button(master, text='-',font=("Calibri, 15"), command=menosFone)
btnRmFone.pack(side ='top')
btnRmFone.place(width=35, height=35, x=230, y=480)


#botão Confirmar
btnConfirmar = Button(master, text='Confirmar',font=("Calibri, 12"), command=cadastroFunc)
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
#Label Data de Contratação
lbldtaContratacao = Label(master,text= "Data de Contratação: ",font = "Calibri, 11",).place(x=300, y=315)
#Label Telefone
lblTelefone = Label(master,text= "Telefone: ",font = "Calibri, 11",).place(x=15, y=375)


master.mainloop()

