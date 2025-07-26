import tkinter as tk

root = tk.Tk()
root.title("Wyśrodkowane okno")

# Domyślny rozmiar okna (możesz też jawnie go podać)
root.geometry("300x200")

# Czekamy aż window manager ustali rozmiary
root.update_idletasks()

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = root.winfo_width()
wh = root.winfo_height()

# Obliczamy pozycję startową
x = (sw - ww) // 2
y = (sh - wh) // 2

root.geometry(f"{ww}x{wh}+{x}+{y}")

root.mainloop()