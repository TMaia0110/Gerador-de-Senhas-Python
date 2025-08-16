import tkinter as tk
from tkinter import messagebox
import string
import pyperclip
import secrets

def gerarSenha():
    try:
        tamanho_senha = int(tamanho.get());
        if tamanho_senha <= 0:
            messagebox.showerror("Erro", "Digite um número inteiro positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números inteiros.")
        return
    
    caracteres = string.ascii_letters + string.digits + string.punctuation;
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho_senha))
    saida.delete(0, tk.END);
    saida.insert(0, senha);

def copiar():
    senha_gerada = saida.get();
    pyperclip.copy(senha_gerada);
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!");


janela = tk.Tk();
janela.title('Gerador de senhas');
janela.geometry('500x250');
janela.config(bg="#0228A3");

tk.Label(janela, text='Gerador de Senha', bg= '#0228A3', fg='white', font =("Nata Sans", 20)).pack(pady=5);
tk.Label(janela, text = 'Digite aqui o tamanho da sua senha', bg = '#0228A3', fg='white', font = ("Nata Sans", 13)).pack(pady=3);
tamanho = tk.Entry(janela);
tamanho.pack(pady=5);
tk.Button(janela, text="Gerar Senha", bg="white", command=gerarSenha).pack(pady=5);
saida = tk.Entry(janela);
saida.pack(pady=5);
tk.Button(janela, text="Copiar Senha", bg="white", command=copiar).pack(pady=5);

janela.mainloop();

#Gerando números de senhas aleatórios
#numeros = secrets.choice(range(0, 100))
#print(secrets.token_hex(10))



