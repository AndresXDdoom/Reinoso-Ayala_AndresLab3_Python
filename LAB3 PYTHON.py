import tkinter as tk
import random

def symbol_weight(symbol):
    if symbol.isalpha():
        return ord(symbol) - 64
    else:
        return int(symbol)
def generate_block():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    while True:
        block = ''
        total = 0
        for i in range(4):
            symbol = random.choice(symbols)
            block += symbol
            total += symbol_weight(symbol)
        if total >= 30 and total <= 35:
            return block
def generate_key():
    block1 = generate_block()
    block2 = generate_block()
    block3 = generate_block()
    key = block1 + '-' + block2 + '-' + block3
    key_label.configure(text=key)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for symbol in block1:
        sum1 += symbol_weight(symbol)
    for symbol in block2:
        sum2 += symbol_weight(symbol)
    for symbol in block3:
        sum3 += symbol_weight(symbol)
    sum_label.configure(
        text=f'Суммы: {sum1} - {sum2} - {sum3}'
    )
def cancel():
    window.destroy()
window = tk.Tk()
window.title('Key Generator')
window.geometry('500x300')
window.configure(bg='lightblue')
title_label = tk.Label(
    window,
    text='KEY GENERATOR',
    font=('Verdana', 20),
    bg='black',
    fg='white'
)
title_label.place(relx=0.5, rely=0.1, anchor='center')
key_label = tk.Label(
    window,
    text='XXXX-XXXX-XXXX',
    font=('Consolas', 25),
    bg='white'
)
key_label.place(relx=0.5, rely=0.35, anchor='center')
sum_label = tk.Label(
    window,
    text='Суммы:',
    font=('Verdana', 12)
)
sum_label.place(relx=0.5, rely=0.52, anchor='center')
btn_generate = tk.Button(
    window,
    text='Generate',
    width=15,
    command=generate_key
)
btn_generate.place(relx=0.2, rely=0.7)
btn_cancel = tk.Button(
    window,
    text='Cancel',
    width=15,
    command=cancel
)
btn_cancel.place(relx=0.58, rely=0.7)
window.mainloop()