from tkinter import *
from tkinter import ttk

root = Tk()
style = ttk.Style(root)
style.theme_use('clam')

# root.geometry("600x600")
root.title("Tic Tac Toe vs AI")
frame = ttk.Frame(root, padding=10)
frame.grid()

def print_clicked():
    print("CLICKED")

buttons = []
for row in range(3):
    rows = []
    for col in range(3):
        button = ttk.Button(root, command = print_clicked, width=20)
        button.grid(row=row, column=col, padx=10, pady=10)
        rows.append(button)
    buttons.append(rows)

root.mainloop()