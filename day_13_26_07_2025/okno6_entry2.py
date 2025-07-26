import tkinter as tk


def get_entry_value():
    text = entry.get()
    print(f"Entered: {text}")


root = tk.Tk()
root.title("Entry Widget Example")
root.geometry("300x150")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

entry.insert(0, "Type here...")

button = tk.Button(root, text="Get Text", command=get_entry_value)
button.pack(pady=5)

root.mainloop()
