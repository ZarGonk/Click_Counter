# Import libraries
import tkinter as tk
from tkinter import ttk
from counter import *

def on_start():
    """Set the counter with the initial value from input and display it."""
    try:
        number = int(value_start.get())
    except ValueError:
        number = 0 
    set_value(number)
    display_and_color()

def display_and_color():
    """Update the label with the current counter value.
       Change background color when the value is a multiple of 10."""
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
    """Reset the counter and restore the initial background color."""
    reset()
    message['text'] = '0'
    root.config(bg=color_lightblue)
    instruction.config(bg=color_lightblue)
    frame_entry.config(bg=color_lightblue)
    text_entry.config(bg=color_lightblue)
    frame.config(bg=color_lightblue)
    message.config(bg=color_lightblue)

# Default background color
color_lightblue = 'lightblue'

# Create the main window
root = tk.Tk()
root.title('Button Click')
root.config(background=color_lightblue)

# Set minimum and maximum window size
root.minsize(280, 170)
root.maxsize(400, 250)

# Window icon
try: 
    photo = tk.PhotoImage(file="assets/mouse_icon.png")
    root.iconphoto(False, photo)
except tk.TclError:
    print('Icon file not found')

# Title label
instruction = tk.Label(root, text='Click Counter',
    font=('Times New Roman', 15, 'italic'),
    bg=color_lightblue
)
instruction.pack(pady=10)

# Entry frame (initial value)
frame_entry = tk.Frame(root, bg=color_lightblue)
frame_entry.pack(pady=10)

# Label for the entry box
text_entry = tk.Label(frame_entry, text='Initial Value: ',
    font=('Arial', 10, 'bold'),
    bg=color_lightblue
)
text_entry.pack(side='left', padx=5)

# Entry for initial value
value_start = ttk.Entry(frame_entry, width=5)
value_start.pack(side='left')
value_start.focus()

# Button to set initial value
button_start = ttk.Button(frame_entry, text='Start Count', command=on_start)
button_start.pack(side='left', padx=10)

# Frame for main buttons
frame = tk.Frame(root, bg=color_lightblue)
frame.pack(pady=10)

# Button to increment the counter
button_click = ttk.Button(frame, text='Count',
    command=lambda: [increment(), display_and_color()])
button_click.pack(side='left', padx=5)

# Button to decrement the counter
button_decrement = ttk.Button(frame, text='Decrement',
    command=lambda: [decrement(), display_and_color()])
button_decrement.pack(side='left', padx=5)

# Button to reset the counter
button_reset = ttk.Button(frame, text='Reset',
    command=on_reset)
button_reset.pack(side='left', padx=5)

# Label to display counter value
message = tk.Label(root, text='0',
                    font=('Arial', 12, 'bold'),
                    fg='Red',
                    bg=color_lightblue)
message.pack()

# Run the application
root.mainloop()
