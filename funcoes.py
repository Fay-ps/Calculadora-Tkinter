import tkinter as tk

#funções - tratamento de erro
def tratar_erro(entrada):
    texto = entrada.get()

    if texto == 'Erro':
        entrada.delete(0, tk.END)

# - operadores
def conferir_operador(operador, entrada):
    texto = entrada.get()
    operadores = ['+', '-', '/', '*']
    if texto: #se texto não estiver vazio
        ultimo = texto[-1]
        if ultimo in operadores:
            if operador != ultimo:
                indice_op = len(texto) - 1
                entrada.delete(indice_op, tk.END)
                entrada.insert(tk.END, operador)
                return
            else:
                return
        else:
            entrada.insert(tk.END, operador)
    else:
        return
    

def conferir_exponenciacao(entrada):
    texto = entrada.get()
    operadores = ('+', '-', '*', '/')
    if texto == '':
        return
    if texto:
        if texto.endswith(operadores) or texto.endswith('**'):
            return
        else:
            entrada.insert(tk.END, '**')


def conferir_sqrt(entrada):
    texto = entrada.get()
    operadores = ('+', '-', '*', '/')

    if texto == '':
        return
    if texto:
        if texto.endswith(operadores):
            return
        else:
            ultimo = texto[-1]
            if ultimo.isdigit() or ultimo == ')':
                entrada.insert(tk.END, '**(0.5)')



def conferir_float(entrada, sdecimal='.'):
    texto = entrada.get()
    if texto == '':
        return
    texto = texto.replace('+', '|')
    texto = texto.replace('-', '|')
    texto = texto.replace('*', '|')
    texto = texto.replace('/', '|')

    partes = texto.split('|')
    if partes: #se texto nao esta vazio
        if sdecimal in partes[-1]: #verificar ultimo número
            return
        else:
            entrada.insert(tk.END, '.')
    else:
        return


# - parentese e numero negativo
def conferir_parenteses(entrada):
    texto = entrada.get()
    
    if texto == '':
        entrada.insert(tk.END, '(')
        return
    
    aberto = texto.count('(')
    fechado = texto.count(')')
    ultimo = texto[-1]

    if aberto > fechado:
        if ultimo.isdigit() or ultimo == ')':
            entrada.insert(tk.END, ')')
        return
    else:
        if ultimo.isdigit() or ultimo == ')':
                entrada.insert(tk.END, '*(')
        else:
            entrada.insert(tk.END, '(')
        return
    


def numero_negativo(entrada):
    texto = entrada.get()
    if texto == '':
        entrada.insert(tk.END, '(-')
    else:
        ultimo = texto[-1]
        if ultimo.isdigit() or ultimo == ')':
            entrada.insert(tk.END, '*(-')
        else:
            entrada.insert(tk.END, '(-')


# - apagar/limpar
def backspace(entrada):
    texto = entrada.get()
    indice_inicio = len(texto) - 1 #onde começa a apagar
    if texto:
        entrada.delete(indice_inicio, tk.END)


# - calcular expressão
def calcular(entrada):
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, 'Erro')


#personalização
def estilo_botao(botao, backg='gray12', backgativo='gray8', fg_ativo='gray75'):
    botao.config(bg=backg, fg='ghost white', font=('Consolas', 14), activebackground=backgativo, activeforeground=fg_ativo, relief='flat', bd=0)