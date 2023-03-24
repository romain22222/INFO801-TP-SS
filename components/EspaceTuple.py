from typing import Dict

from .EssenceType import EssenceType
from .ObjectConnectable import ObjectConnectable


class EspaceTupleInfo:
    def __init__(self, essence: EssenceType, qte: float):
        self.essence = essence
        self.qte = qte

    def __str__(self):
        return f"Ticket :\n- Essence: {self.essence}\n- Qté restante: {self.qte}"


class EspaceTuple(ObjectConnectable):
    def __init__(self) -> 'EspaceTuple':
        ObjectConnectable.__init__(self)
        self.codes: Dict[str, EspaceTupleInfo] = {}

    def ajouterCode(self, code: str, essence: EssenceType, qte: float):
        self.codes[code] = EspaceTupleInfo(essence, qte)

    def editerCode(self, code: str, qteRestante: float):
        if qteRestante == 0:
            del self.codes[code]
        else:
            self.codes[code] = EspaceTupleInfo(self.codes[code].essence, qteRestante)

    def getCode(self, code: str) -> EspaceTupleInfo:
        return self.codes[code]
