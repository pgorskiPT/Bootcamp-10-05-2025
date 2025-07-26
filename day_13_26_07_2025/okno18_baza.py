import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_data():
    # połączenie z bazą
    conn = sqlite3.connect('moja_baza.db')
    cur = conn.cursor()
    cur.execute('SELECT id, nazwa, Field3 FROM przyklad;')
    rows = cur.fetchall()
    conn.close()
    return rows

root = tk.Tk()
root.title("Dane z SQLite")

# definiujemy kolumny
columns = ('id', 'nazwa', 'wartosc')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.pack(fill=tk.BOTH, expand=True)

# nagłówki
tree.heading('id', text='ID')
tree.heading('nazwa', text='Nazwa')
tree.heading('wartosc', text='Wartość')

# szerokości kolumn
tree.column('id', width=50, anchor=tk.CENTER)
tree.column('nazwa', width=150, anchor=tk.W)
tree.column('wartosc', width=100, anchor=tk.E)

# wczytanie i wstawienie danych
for row in fetch_data():
    tree.insert('', tk.END, values=row)

root.mainloop()