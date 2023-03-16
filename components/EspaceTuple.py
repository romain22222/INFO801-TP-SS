from typing import Dict

from .EssenceType import EssenceType
from .ObjectConnectable import ObjectConnectable


class EspaceTupleInfo:
    def __init__(self, essence: EssenceType, qte: float):
        self.essence = essence
        self.qte = qte


class EspaceTuple(ObjectConnectable):
    def __init__(self) -> 'EspaceTuple':
        super()
        self.codes: Dict[str, EspaceTupleInfo] = {}

    def ajouterCode(self, code: str, essence: EssenceType, qte: float):
        self.codes[code] = EspaceTupleInfo(essence, qte)

    def editerCode(self, code: str, qteRestante: float):
        if qteRestante == 0:
            del self.codes[code]
        else:
            self.codes[code] = EspaceTupleInfo(self.codes[code][0], qteRestante)

    def getCode(self, code: str) -> EspaceTupleInfo:
        return self.codes[code]
