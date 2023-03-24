class Ticket:
    def __init__(self, code: str, qte: float) -> 'Ticket':
        self.code = code
        self.qte = qte

    def __str__(self) -> str:
        return f"Ticket: code={self.code}, qte={self.qte}"
