from components.EssenceType import EssenceType
from components.StationService import StationService


def displayChoices():
    while True:
        print("Que voulez-vous faire ?")
        print("1 - Acheter du carburant")
        print("2 - Faire un plein")
        print("3 - Voir les informations d'un ticket")
        print("4 - Quitter")
        userInputDC = input("Votre choix : \n")
        print()
        if userInputDC in "1234":
            return userInputDC
        print("\033[91;1;4;5;53;58;5;31mChoix invalide !\033[0m\n")


def getUserEssence():
    while True:
        essence = input("Essence : \n")
        if int(essence) in range(1, 10):
            return list(EssenceType.__members__.keys())[int(essence) - 1]
        elif essence in EssenceType.__members__.keys():
            return essence
        print("\033[91;1;4;5;53;58;5;31mEssence invalide !\033[0m\n")


def acheterEssence():
    print("Quelle essence voulez-vous acheter et quelle quantité ?")
    i = 1
    for e in EssenceType.__members__.keys():
        print(f"{i} - {e}")
        i += 1
    essence = getUserEssence()
    prix = float(input("Quel somme voulez-vous mettre : \n"))

    print(f"Vous avez choisi de payer pour {prix}€ de {essence}.\n")
    ticket = station.acheterEssence(prix, essence)
    print(ticket)


def faireLePlein():
    code, t = infosTicket()
    while True:
        nPompe = int(input("Quelle pompe ?\n"))
        if nPompe in range(station.nbPompes):
            break
        print("Mauvais numéro de pompe ! Veuillez en spécifier une valide")
    cbLitres = float(input("Combien de litres voulez-vous retirer ?\n"))
    res = station.remplirReservoir(code, cbLitres, nPompe)
    if res.qte < 0:
        print(f"Vous n'avez pas pu remplir votre réservoir au maximum, il vous manque {-res.qte} litres")
    elif res.qte > 0:
        print(f"Il vous reste {res.qte} litres sur ce code")
    else:
        print(f"Le code a complètement été vidé")
    pass


def infosTicket():
    code = input("Sur quel ticket ?\n")
    try:
        t = station.getInfos(code)
        print(t)
    except Exception:
        t = None
        print("Aucun ticket n'est relié à ce code")
    print()
    return code, t


def manageInput(userInputMI):
    match userInputMI:
        case "4":
            return False
        case "1":
            acheterEssence()
        case "2":
            faireLePlein()
        case "3":
            infosTicket()
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    keepRefill = True
    station = StationService(6)

    while keepRefill:
        userInput = displayChoices()
        keepRefill = manageInput(userInput)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
