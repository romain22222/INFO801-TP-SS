from .EspaceTuple import EspaceTuple
from .ObjectConnectable import ObjectConnectable
from .Ticket import Ticket


class Pompe(ObjectConnectable):
    def __init__(self, et: EspaceTuple) -> 'Pompe':
        ObjectConnectable.__init__(self)
        self.addConnexion("EspaceTuple", et)  # Telephone maison

    def faireLePlein(self, code: str, quantite: float) -> Ticket:
        et = self.getConnexion("EspaceTuple")
        info = et.getCode(code)
        qteSave = info.qte
        et.editerCode(code, qteSave - quantite if qteSave >= quantite else 0)
        return Ticket(code, qteSave - quantite)
