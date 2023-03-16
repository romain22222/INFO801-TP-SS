class ObjectConnectable:
    def __init__(self) -> 'ObjectConnectable':
        self.connexions = {}

    def addConnexion(self, name: str, objectToConnect: 'ObjectConnectable'):
        self.connexions[name] = objectToConnect

    def removeConnexion(self, name: str):
        del self.connexions[name]

    def getConnexion(self, name):
        return self.connexions[name] if name in self.connexions.keys() else None

