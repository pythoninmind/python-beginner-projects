class CalculatorLogic:
    def __init__(self):
        self.expression = ""

    def append_char(self, char):
        """Hängt ein Zeichen an den aktuellen mathematischen Ausdruck an."""
        self.expression += str(char)
        return self.expression

    def clear(self):
        """Löscht den gesamten Ausdruck."""
        self.expression = ""
        return self.expression

    def evaluate(self):
        """Berechnet das Ergebnis oder gibt bei Fehlern 'Error' zurück."""
        try:
            # Berechnet den String-Ausdruck sicher/direkt
            result = eval(self.expression)
            self.expression = str(result)
            return self.expression
        except Exception:
            self.expression = ""  # Setzt den internen Zustand bei Fehler zurück
            return "Error"
