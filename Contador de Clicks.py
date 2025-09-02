# Importar as bibliotecas 
import tkinter as tk
from tkinter import ttk
from random import randint

# Criar uma função para contar os clicks
color = ''
count = 0
def click():
    global count
    count +=1
    message['text'] = f'You Clicked {count} times'
    return message['text'] 

# Criar uma função para decrementar os click
def decrement():
    global count
    count -= 1
    message['text'] = f'You Clicked {count} times'  
    return message['text']

# Criar uma função para resetar o contador
def reset():
    global count 
    count = 0
    message['text'] = 0
    return message['text']

def start():
    global count
    starter = int(count.get())
    message['text'] = starter
    return message['text']

# Gerador de cor aleatoria 
"VOLTAR AQUIIIII COLOCAR ESTA FUNÇÃO"
def color_hex_random():
    return '#{:06x}'.format(randint(0, 0xFFFFFF))

# Cria uma janela
root = tk.Tk()
root.title('Button Click')
root.config(background='lightblue')

#Crial um label de instrução
instruction = tk.Label(
    root,
    text='Click Counter',
    font=('Times New Roman', 15, 'italic'),
    bg='lightblue'
)
instruction.pack(pady=10)

# Alinhar Entry
frame_entry = tk.Frame(root, bg='Lightblue')
frame_entry.pack(pady=10)

value_start = ttk.Entry(frame_entry, width=5)
value_start.focus()
value_start.pack(side='right')

# Texto Label Instrução para entrada do contador
text_entry = tk.Label(
    frame_entry, 
    text='Valor Inicial: ',
    font=('Arial', 10, 'bold'),
    bg='lightblue'
)
text_entry.pack(side='left', padx=5)

button_start = ttk.Button(frame_entry, text='Start count', command=start)
button_start.pack(padx= 15)





# Alinhar os bottons
frame = tk.Frame(root, bg='lightblue')
frame.pack(pady=15)

# Criar um Button para clicar e contar a quantia de click
button_click = ttk.Button(
    frame,
    text='Count',
    command=click)
button_click.pack(side= 'left', padx=5)

button_decrement = ttk.Button(
    frame,
    text='Decrement',
    command=decrement
)
button_decrement.pack(side='left', padx=5)


# Criar um Button para resetar a contagem
button_reset = ttk.Button(
    frame,
    text='Reset',
    command=reset
)
button_reset.pack(side='left', padx=5)

# Criar um Label para exibir o numero de clicks
message = tk.Label(
    root,
    text='0',
    font=('Arial',12, 'bold'),
    fg='Red',
    bg='lightblue'
)
message.pack()

root.mainloop()