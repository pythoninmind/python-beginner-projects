import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Taschenrechner")
        self.geometry("300x400")
        self.configure(bg="#2e2e2e")
        
        # Aktiviert das responsive Layout (Fenstergröße veränderbar)
        self.resizable(True, True) 
        
        self.custom_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display oben (Dark Theme)
        display = tk.Entry(
            self, 
            textvariable=self.result_var, 
            font=self.custom_font, 
            bg="#1e1e1e", 
            fg="#ffffff", 
            bd=0, 
            justify="right"
        )
        display.pack(fill="both", padx=10, pady=20, ipady=10)

        # Button-Layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]

        # Erstellt die Buttons (Responsive durch expand=True und fill=both)
        for row in buttons:
            frame = tk.Frame(self, bg="#2e2e2e")
            frame.pack(expand=True, fill="both")
            for btn_text in row:
                btn = tk.Button(
                    frame, 
                    text=btn_text, 
                    font=self.custom_font, 
                    bg="#3e3e3e", 
                    fg="#ffffff", 
                    bd=0, 
                    relief="flat", 
                    command=lambda txt=btn_text: self.on_click(txt)
                )
                btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def on_click(self, char):
        # Display leeren
        if char == "C":
            self.result_var.set("")
        # Berechnung ausführen
        elif char == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception:
                # Fehlerbehandlung bei ungültigen Ausdrücken
                self.result_var.set("Error")
        # Zeichen anhängen
        else:
            current = self.result_var.get()
            self.result_var.set(current + char)

