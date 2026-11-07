import tkinter as tk
from tkinter import font
from logic import CalculatorLogic  # Importiert die Logik

class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Taschenrechner")
        self.geometry("300x400")
        self.configure(bg="#2e2e2e")
        self.resizable(True, True) 
        
        # Instanz der Logik-Klasse erstellen
        self.logic = CalculatorLogic()
        
        self.custom_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display (Dark Theme)
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

        # Buttons erstellen (Responsive)
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
                    command=lambda txt=btn_text: self.on_button_click(txt)
                )
                btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def on_button_click(self, char):
        # Leitet die Aktionen an die Logik-Klasse weiter
        if char == "C":
            new_text = self.logic.clear()
        elif char == "=":
            new_text = self.logic.evaluate()
        else:
            # Falls vorher ein Error im Display stand, leeren wir es für die neue Eingabe
            if self.result_var.get() == "Error":
                self.logic.clear()
            new_text = self.logic.append_char(char)
            
        # Aktualisiert die GUI-Anzeige
        self.result_var.set(new_text)

