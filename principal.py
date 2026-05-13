#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Calculadora Tkinter | Primeiro projeto GUI(05/2026)
#Desenvolvido por Fay
#LinkedIn:
#www.linkedin.com/in/pedro-fay-schenlrte-67b453365
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import tkinter as tk
import funcoes as fc


janela = tk.Tk()
janela.config(background='gray7', bd=0)
janela.title('Calculadora') #nome do app
janela.geometry('300x500') #largura X altura
janela.grid_rowconfigure(0, weight=3)
for c in range(1, 7):
    janela.grid_rowconfigure(c, weight=1)
for c in range(0, 4):
    janela.grid_columnconfigure(c, weight=1)

#entrada de valores
entrada = tk.Entry(janela)
entrada.grid(row=0, column=0, columnspan=4, sticky='nsew')
entrada.config(background='gray10', fg='ghost white', font=('Consolas', 14), bd=0, justify='right')

#botões - numeros
for numero in range(1,10):
    botaonumeros = tk.Button(janela, text=f'{numero}', command= lambda n=numero: (fc.tratar_erro(entrada), entrada.insert(tk.END, n))) #variavel 'n' é para guardar o valor da variavel 'numero', sem isso o valor não é guardado e é exibido somente o ultimo valor(9)
    indice = numero-1
    linha = (indice // 3) + 2
    coluna = indice % 3
    fc.estilo_botao(botaonumeros)
    botaonumeros.grid(row=linha, column=coluna, sticky='nsew') #posicionamento

botao0 = tk.Button(janela, text='0', command= lambda: (fc.tratar_erro(entrada), entrada.insert(tk.END, 0)))
botao0.grid(row=5, column=1, sticky='nsew') #posição fixa(linha e coluna começam do n°0)

# - operadores
operadores = ['+', '-', '/', '*']

for i, operador in enumerate(operadores):
    botaoop = tk.Button(janela, text=f'{operador}', command= lambda op=operador: (fc.tratar_erro(entrada), fc.conferir_operador(op, entrada)))
    fc.estilo_botao(botaoop, backg='dark orange', backgativo='DarkOrange3')
    botaoop.grid(row=i+2, column=3, sticky='nsew')

# - exponenciação ex:n²
botaoexp = tk.Button(janela, text= 'Xʸ', command= lambda: (fc.tratar_erro(entrada), fc.conferir_exponenciacao(entrada)))
botaoexp.grid(row=6, column=2, sticky='nsew')

# - raiz quadrada
botaosqrt = tk.Button(janela, text= '√', command= lambda: (fc.tratar_erro(entrada), fc.conferir_sqrt(entrada)))
botaosqrt.grid(row=6, column=1, sticky='nsew')

# - decimal
botaofloat = tk.Button(janela, text=',', command= lambda: (fc.tratar_erro(entrada), fc.conferir_float(entrada=entrada)))
botaofloat.grid(row=5, column=2, sticky='nsew')

# - parentese e negativo
botaoparenteses = tk.Button(janela, text= '()', command= lambda: (fc.tratar_erro(entrada), fc.conferir_parenteses(entrada)))
botaoparenteses.grid(row=5, column=0, sticky='nsew')

botaonegativo = tk.Button(janela, text= '(-', command= lambda: (fc.tratar_erro(entrada), fc.numero_negativo(entrada)))
botaonegativo.grid(row=6, column=0, sticky='nsew')

# - apagar conta/numero
botaoapagar = tk.Button(janela, text='<-', command= lambda: (fc.tratar_erro(entrada), fc.backspace(entrada)))
botaoapagar.grid(row=1, column=3, sticky='nsew')

botaoClear = tk.Button(janela, text='C', command= lambda: (fc.tratar_erro(entrada), entrada.delete(0, tk.END)))
botaoClear.grid(row=1, column=0, sticky='nsew')
fc.estilo_botao(botaoClear, backg='firebrick3', backgativo='firebrick4')

# - calcula expressão
botaoigual = tk.Button(janela, text='=', command= lambda: (fc.tratar_erro(entrada), fc.calcular(entrada)))
botaoigual.grid(row=6, column=3, sticky='nsew')
fc.estilo_botao(botaoigual, backg='blue', backgativo='navy')

# - personalização geral
botoes = [botaoapagar, botaosqrt, botaofloat, botaoexp, botao0, botaonegativo, botaoparenteses]
for b in botoes:
    fc.estilo_botao(b)

#adicionado ao final para manter a janela aberta e aceitar atualizações no código
janela.mainloop()

