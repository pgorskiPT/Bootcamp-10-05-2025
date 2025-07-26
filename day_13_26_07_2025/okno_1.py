import tkinter as tk

# mvc

# tworzenie okna
root = tk.Tk()

# ustawic tytuł okna
root.title("My First Tkinter App")

# wielkośc okna
# root.geometry("400x300")
# root.geometry("<szerokość>x<wysokość>+<pozycja_x>+<pozycja_y>")
root.geometry("400x300+100+100")

# uruchumienie okna
root.mainloop()
