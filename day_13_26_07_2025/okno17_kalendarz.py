import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime


class CustomEntry(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master)
        style = ttk.Style()
        style.configure("Custom.TEntry", fieldbackground='#ffffff', foreground='#333333')
        style.configure("Custom.TButton", fieldbackground='#dddddd', foreground='#333333')

        self.var = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.var,
                               style='Custom.TEntry', width=16)
        self.entry.pack(side="left", fill='x', expand=True)

        self.btn = ttk.Button(self, text="▼", command=self.show_calendar,
                              style="Custom.TButton", width=2)
        self.btn.pack(side="left")

        self.entry.bind('<Button-1>', lambda e: self.show_calendar())
        self.calendar_win = None

    def show_calendar(self):
        pass