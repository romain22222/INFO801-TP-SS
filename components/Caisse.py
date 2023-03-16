import math
import random

from .EspaceTuple import EspaceTuple
from .EssenceType import EssenceType
from .Ticket import Ticket
from .ObjectConnectable import ObjectConnectable


class Caisse(ObjectConnectable):
    def __init__(self, et: EspaceTuple):
        super()
        self.addConnexion("EspaceTuple", et)
        self.conversionPrices = [random.random()+1 for _ in range(EssenceType.__len__())]

    @classmethod
    def generateCode(cls) -> str:
        chars = ['abcdefghijklmnopqrstuvwxyz0123456789']
        return str([chars[math.round(random.random()*len(chars))] for _ in range(16)])

    def acheterEssence(self, prix: float, essence: EssenceType) -> Ticket:
        code = Caisse.generateCode()
        qte = prix/self.conversionPrices[essence]
        self.getConnexion("EspaceTuple").ajouterCode(code, essence, qte)
        return Ticket(code, qte)



