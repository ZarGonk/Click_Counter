# Importar as bibliotecas 
import tkinter as tk
from tkinter import ttk
from counter import *

def on_start():
    try:
        number = int(value_start.get())
    except ValueError:
        number = 0 
    set_value(number)
    display_and_color()


def display_and_color():
    value = get_value()
    message['text'] = str(value)

    if value != 0 and value % 10 == 0:
        new_color = color_hex_random()
        root.config(bg=new_color)
        instruction.config(bg=new_color)
        frame_entry.config(bg=new_color)
        text_entry.config(bg=new_color)
        frame.config(bg=new_color)
        message.config(bg=new_color)


def on_reset():
    reset()
    message['text'] = '0'
    # volta para cor inicial
    root.config(bg=color_lightblue)
    instruction.config(bg=color_lightblue)
    frame_entry.config(bg=color_lightblue)
    text_entry.config(bg=color_lightblue)
    frame.config(bg=color_lightblue)
    message.config(bg=color_lightblue)


color_lightblue = 'lightblue'

# Cria uma janela
root = tk.Tk()
root.title('Button Click')
root.config(background=color_lightblue)


# Tamanho minimo e maximo
root.minsize(280, 170)
root.maxsize(400, 250)

# Icon para janela
try: 
    photo = tk.PhotoImage(file="assets/mouse_icon.png")
    root.iconphoto(False, photo)
except tk.TclError:
    print('icon file not found')


# Label de título
instruction = tk.Label(root, text='Click Counter',
    font=('Times New Roman', 15, 'italic'),
    bg=color_lightblue
)
instruction.pack(pady=10)

# Frame de Entrada inicial
frame_entry = tk.Frame(root, bg=color_lightblue)
frame_entry.pack(pady=10)

# Texto do Entry de instrução 
text_entry = tk.Label(frame_entry, text='Valor Inicial: ',
    font=('Arial', 10, 'bold'),
    bg=color_lightblue
)
text_entry.pack(side='left', padx=5)

# Entry para o valor inicial
value_start = ttk.Entry(frame_entry, width=5)
value_start.pack(side='left')
value_start.focus()

button_start = ttk.Button(frame_entry, text='Start Count', command=on_start)
button_start.pack(side='left', padx= 10)

# Frame de Botões
frame = tk.Frame(root, bg=color_lightblue)
frame.pack(pady=10)

# Botão para incrementar o contador
button_click = ttk.Button(frame, text='Count',
    command=lambda: [increment(), display_and_color()])
button_click.pack(side= 'left', padx=5)

# Botão para decrementar o contador
button_decrement = ttk.Button(frame, text='Decrement',
    command=lambda: [decrement(), display_and_color()])
button_decrement.pack(side='left', padx=5)

# Botão para resetar o contador
button_reset = ttk.Button(frame, text='Reset',
    command= on_reset)
button_reset.pack(side='left', padx=5)


# Criar um Label para exibir o numero de clicks
message = tk.Label(root, text='0',
                    font=('Arial',12, 'bold'),
                    fg='Red',
                    bg=color_lightblue)
message.pack()

root.mainloop()