import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class Servico(ABC):
    def __init__(self, nome_sobrenome, horario, celular):
        self.nome_sobrenome = nome_sobrenome
        self.horario = horario
        self.celular = celular

    @abstractmethod
    def mostrar(self):
        pass

class Cabelo(Servico):
    def mostrar(self):
        return f"Cabelo | Nome: {self.nome_sobrenome} | Horário: {self.horario} | Celular: {self.celular} | Preço: R$25"

class Barba(Servico):
    def mostrar(self):
        return f"Barba | Nome: {self.nome_sobrenome} | Horário: {self.horario} | Celular: {self.celular} | Preço: R$20"

class Sobrancelha(Servico):
    def mostrar(self):
        return f"Sobrancelha | Nome: {self.nome_sobrenome} | Horário: {self.horario} | Celular: {self.celular} | Preço: R$10"

class CabeloEBarba(Servico):
    def mostrar(self):
        return f"Cabelo e Barba | Nome: {self.nome_sobrenome} | Horário: {self.horario} | Celular: {self.celular} | Preço: R$40"

class CabeloESobrancelha(Servico):
    def mostrar(self):
        return f"Cabelo e Sobrancelha | Nome: {self.nome_sobrenome} | Horário: {self.horario} | Celular: {self.celular} | Preço: R$30"

class BarbaESobrancelha(Servico):
    def mostrar(self):
        return f"Barba e Sobrancelha | Nome: {self.nome_sobrenome} | Horário: {self.horario} | Celular: {self.celular} | Preço: R$25"

class CabeloBarbaESobrancelha(Servico):
    def mostrar(self):
        return f"Cabelo, Barba e Sobrancelha | Nome: {self.nome_sobrenome} | Horário: {self.horario} | Celular: {self.celular} | Preço: R$50"

servicos = []

def cadastrar_servico():
    tipo = tipo_var.get()
    nome_sobrenome = nome_entry.get().strip()
    horario = horario_entry.get().strip()
    celular = celular_entry.get().strip()

    if not nome_sobrenome or not horario or not celular:
        mensagem_label["text"] = "Por favor, preencha todos os campos!"
        mensagem_label["foreground"] = "red"
        return

    try:
        dia, hora = horario.split(" ")
        dia_valido = list(map(int, dia.split("/"))) 
        hora_valida = list(map(int, hora.split(":")))  
    except ValueError:
        mensagem_label["text"] = "Horário inválido! Use o formato DD/MM HH:MM"
        mensagem_label["foreground"] = "red"
        return

    servico = None
    if tipo == "Cabelo":
        servico = Cabelo(nome_sobrenome, horario, celular)
    elif tipo == "Barba":
        servico = Barba(nome_sobrenome, horario, celular)
    elif tipo == "Sobrancelha":
        servico = Sobrancelha(nome_sobrenome, horario, celular)
    elif tipo == "Cabelo e Barba":
        servico = CabeloEBarba(nome_sobrenome, horario, celular)
    elif tipo == "Cabelo e Sobrancelha":
        servico = CabeloESobrancelha(nome_sobrenome, horario, celular)
    elif tipo == "Barba e Sobrancelha":
        servico = BarbaESobrancelha(nome_sobrenome, horario, celular)
    elif tipo == "Cabelo, Barba e Sobrancelha":
        servico = CabeloBarbaESobrancelha(nome_sobrenome, horario, celular)

    if servico:
        servicos.append(servico)
        atualizar_lista()
        limpar_campos()
        mensagem_label["text"] = f"Serviço '{tipo}' cadastrado com sucesso! Preço: {servico.mostrar().split('| Preço: ')[1]}"
        mensagem_label["foreground"] = "yellow"

def atualizar_lista():
    lista_texto.delete(*lista_texto.get_children())
    for i, servico in enumerate(servicos, start=1):
        lista_texto.insert("", "end", values=(i, servico.mostrar()))

def limpar_campos():
    nome_entry.delete(0, tk.END)
    horario_entry.delete(0, tk.END)
    celular_entry.delete(0, tk.END)
    tipo_var.set("Cabelo")

janela = tk.Tk()
janela.title("Barbearia do Rômulo")
janela.geometry("800x600")
janela.configure(bg="#333333")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#333333", foreground="white", font=("Helvetica", 12))
style.configure("TButton", background="#444444", foreground="white", font=("Helvetica", 12), padding=5)

titulo_label = tk.Label(janela, text="💈 Barbearia do Rômulo 💈", bg="#444444", fg="#FFD700", font=("Helvetica", 16, "bold"))
titulo_label.pack(pady=10, fill="x")

notebook = ttk.Notebook(janela)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

aba_cadastro = ttk.Frame(notebook)
notebook.add(aba_cadastro, text="Cadastro de Serviços")

cadastro_frame = ttk.Frame(aba_cadastro, padding=20)
cadastro_frame.pack(fill="both", expand=True)

ttk.Label(cadastro_frame, text="Tipo de Serviço:").grid(row=0, column=0, sticky="w", pady=5)
tipo_var = tk.StringVar(value="Cabelo")
tipo_menu = ttk.Combobox(cadastro_frame, textvariable=tipo_var, values=[
    "Cabelo", "Barba", "Sobrancelha", 
    "Cabelo e Barba", "Cabelo e Sobrancelha", 
    "Barba e Sobrancelha", "Cabelo, Barba e Sobrancelha"], state="readonly")
tipo_menu.grid(row=0, column=1, sticky="ew", pady=5)

ttk.Label(cadastro_frame, text="Nome e Sobrenome:").grid(row=1, column=0, sticky="w", pady=5)
nome_entry = ttk.Entry(cadastro_frame)
nome_entry.grid(row=1, column=1, sticky="ew", pady=5)

ttk.Label(cadastro_frame, text="Horário (DD/MM HH:MM):").grid(row=2, column=0, sticky="w", pady=5)
horario_entry = ttk.Entry(cadastro_frame)
horario_entry.grid(row=2, column=1, sticky="ew", pady=5)

ttk.Label(cadastro_frame, text="Celular:").grid(row=3, column=0, sticky="w", pady=5)
celular_entry = ttk.Entry(cadastro_frame)
celular_entry.grid(row=3, column=1, sticky="ew", pady=5)

cadastrar_button = ttk.Button(cadastro_frame, text="Cadastrar", command=cadastrar_servico)
cadastrar_button.grid(row=4, column=0, columnspan=2, pady=15)

mensagem_label = ttk.Label(cadastro_frame, text="", font=("Helvetica", 10, "italic"))
mensagem_label.grid(row=5, column=0, columnspan=2)

cadastro_frame.columnconfigure(1, weight=1)

aba_lista = ttk.Frame(notebook)
notebook.add(aba_lista, text="Lista de Serviços")

lista_frame = ttk.Frame(aba_lista, padding=20)
lista_frame.pack(fill="both", expand=True)

lista_texto = ttk.Treeview(lista_frame, columns=("ID", "Detalhes"), show="headings", height=15)
lista_texto.heading("ID", text="ID")
lista_texto.column("ID", width=50, anchor="center")
lista_texto.heading("Detalhes", text="Detalhes")
lista_texto.column("Detalhes", width=600, anchor="w")
lista_texto.pack(fill="both", expand=True)

rodape = tk.Frame(janela, bg="#444444", height=40)
rodape.pack(side="bottom", fill="x")
tk.Label(rodape, text="💈 Desenvolvido por Rômulo Vargas 💈", bg="#444444", fg="#FFD700", font=("Helvetica", 10)).pack()

janela.mainloop()
