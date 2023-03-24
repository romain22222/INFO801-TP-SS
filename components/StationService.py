from Caisse import Caisse
from EspaceTuple import EspaceTuple
from EssenceType import EssenceType
from ObjectConnectable import ObjectConnectable
from Pompe import Pompe
from Ticket import Ticket


class WrongPompeNumber(Exception):
    pass


class StationService(ObjectConnectable):
    def __init__(self, nbPompes: int):
        ObjectConnectable.__init__(self)
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
        for i in range(nb):
            self.addConnexion(f"Pompe{i}", Pompe(et))
