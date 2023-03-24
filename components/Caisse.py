import math
import random

from .EspaceTuple import EspaceTuple
from .EssenceType import EssenceType
from .ObjectConnectable import ObjectConnectable
from .Ticket import Ticket


class Caisse(ObjectConnectable):
    def __init__(self, et: EspaceTuple):
        ObjectConnectable.__init__(self)
        self.addConnexion("EspaceTuple", et)
        self.conversionPrices = [random.random() + 1 for _ in range(EssenceType.__len__())]

    @classmethod
    def generateCode(cls) -> str:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join([chars[math.floor(random.random() * len(chars))] for _ in range(16)])

    def acheterEssence(self, prix: float, essence: EssenceType) -> Ticket:
        code = Caisse.generateCode()
        qte = prix / self.conversionPrices[dir(EssenceType).index(essence)]
        self.getConnexion("EspaceTuple").ajouterCode(code, essence, qte)
        return Ticket(code, qte)
