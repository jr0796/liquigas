
from funcionario import *

#end Point : https://viacep.com.br/
#http://viacep.com.br/ws/01001000/json/

def namefocusOut(event):
    #cep = txtCep.get()
    def buscador():

        #cep = '08490000'
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



