import tkinter as tk
from math import *

def calcular():
    try:
        resultado = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def limpiar():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora Avanzada")
root.geometry("400x600")
root.config(bg="#282c34")

entry = tk.Entry(root, width=25, font=("Helvetica", 28), borderwidth=5, bg="#3e4451", fg="#61dafb")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

def on_entry_click(event):
    entry.config(fg="#61dafb")

entry.bind("<FocusIn>", on_entry_click)

# Botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('sqrt', 5, 0), ('**', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
    ('tan', 6, 0), ('(', 6, 1), (')', 6, 2), ('C', 6, 3),
]

button_color = "#61dafb"
button_active_color = "#56b1d9"

for (text, row, column) in botones:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 16),
                           bg=button_color, fg="black", activebackground=button_active_color,
                           command=calcular)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 16),
                           bg="#ff6f61", fg="white", activebackground="#ff4f4f",
                           command=limpiar)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 16),
                           bg=button_color, fg="black", activebackground=button_active_color,
                           command=lambda t=text: entry.insert(tk.END, t))

    button.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
