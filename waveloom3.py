#codigo aula:
# from tkinter import Button, Tk
# def botao_clicado() :
#     print("0 botão foi clicado!")
# janela = Tk()
# janela.title("Exemplo de Tkinter")
# janela.geometry("300x200")
# botao = Button(janela, text="Clique aqui", command=botao_clicado)
# botao.pack()
# janela.mainloop()

#
# meu:
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=300)
# frm.grid()
# root.geometry("500x600")
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()


from tkinter import *
from tkinter import Tk

root = Tk()

class TelaInicial:
    def __init__(self):
        self.root = root #return root
        self.telaIncial() #mostrando a def da janela
        self.botoes()
        root.mainloop()

    def telaIncial(self):
        self.root.title("Waveloom")
        self.root.geometry("1000x700")

    def botoes(self):
        self.btInicio = Button(text="Vamos começar!", command=app_iniciado).grid(column=1, row=0)



class CadastroPessoa:
    def __init__(self, janela):
        self.root = janela  #return root
        self.cadastroPessoa() #mostrando a def da janela
        self.botoes()
        self.entradas()
        root.mainloop()
    def entradas(self):
        self.email = Label(text="Email:").grid(column=3, row=2)
        self.email2 = Entry(width=35).grid(column=3, row=3)
        self.senha = Label(text="Senha:").grid(column=3, row=4)
        self.senha2 = Entry(width=35).grid(column=3, row=5)
        self.celComercial = Label(text="Telefone comercial:").grid(column=3, row=6)
        self.celComercial2 = Entry(width=35).grid(column=3, row=7)
        self.cnpj = Label(text="CNPJ:").grid(column=3, row=8)
        self.cnpj2 = Entry(width=35).grid(column=3, row=9)

    def cadastroPessoa(self):
        self.root.title("Cadastro pessoa")
        self.root.geometry("1000x700")
    def botoes(self):
        Button(text="Continuar", command=app_timeline).grid(column=2, row=0)


class Timeline:
    def __init__(self, feed):
        self.root = feed
        self.timeline()
        self.entreTml()
        self.btTML()
        root.mainloop()
    def timeline(self):
        self.root.title("Timeline")
        self.root.geometry("1000x700")
    def entreTml(self):
        Label(text="Email:").grid(column=3, row=2)
        Entry(width=35).grid(column=3, row=3)
    def btTML(self):
        self.btONG = Button(text="ONG").grid(column=3, row=1)
        self.btVolun= Button(text="Voluntários").grid(column=4, row=1)



def app_iniciado() :
     root.destroy()
     segundaJanela = Tk()
     CadastroPessoa(segundaJanela)
     segundaJanela.mainloop()

def app_timeline():
    terceiraJanela = Tk()
    Timeline(terceiraJanela)
    terceiraJanela.mainloop()

TelaInicial()