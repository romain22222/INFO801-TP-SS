from .ObjectConnectable import ObjectConnectable
from .Ticket import Ticket
from .EspaceTuple import EspaceTuple


class Pompe(ObjectConnectable):
    def __init__(self, et: EspaceTuple) -> 'Pompe':
        super()
        self.addConnexion("EspaceTuple", et)  # Telephone maison

    def faireLePlein(self, code: str, quantite: float) -> Ticket:
        pass
