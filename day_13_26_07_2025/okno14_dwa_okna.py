import tkinter as tk

root = tk.Tk()
root.title("Główne okno")

label1 = tk.Label(root, text="To jest główne okno")
label1.pack(padx=10, pady=10)

second_window = tk.Toplevel(root)
second_window.title("Drugie okno")

label2 = tk.Label(second_window, text="To jest drugie okno")
label2.pack(padx=10, pady=10)

root.mainloop()
