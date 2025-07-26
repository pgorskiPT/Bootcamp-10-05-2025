import tkinter as tk


def on_click():
    print("Przycisk został naciśnięty")


app = tk.Tk()
app.title("Przykład")
app.geometry("300x200")
# do okienka dodajemy Button
button = tk.Button(app, text="Kliknij mnie", command=on_click)  # podajemy referencje funkcji

button.pack()

app.mainloop()
