from .EssenceType import EssenceType
from .EspaceTuple import EspaceTuple
from .ObjectConnectable import ObjectConnectable
from .Caisse import Caisse
from .Pompe import Pompe
from .Ticket import Ticket


class WrongPompeNumber(Exception):
    pass


class StationService(ObjectConnectable):
    def __init__(self, nbPompes: int):
        super()
        et = EspaceTuple()
        self.addConnexion("EspaceTuple", et)
        self.addConnexion("Caisse", Caisse(et))
        self.ajouterPompe(nbPompes, et)
        self.nbPompes = nbPompes

    def acheterEssence(self, prix: float, essence: EssenceType) -> Ticket:
        if prix <= 0:
            return None
        return self.getConnexion("Caisse").acheterEssence(prix, essence)

    def remplirReservoir(self, code: str, qte: float, pompeNb: int) -> Ticket:
        if not 0 <= pompeNb < self.nbPompes:
            raise WrongPompeNumber()
        return self.getConnexion(f"Pompe{pompeNb}").faireLePlein(code, qte)

    def ajouterPompe(self, nb: int, et: EspaceTuple):
        for i in nb:
            self.addConnexion(f"Pompe{i}", Pompe(et))



