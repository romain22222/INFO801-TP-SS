from components.StationService import StationService
from components.EssenceType import EssenceType
from components.Caisse import Caisse


# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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
        if essence in "123456789":
            return dir(EssenceType)[int(essence)-1]
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
    nPompe = input("Quelle pompe ?")
    code = input("Quel est le code de votre ticket ?\n")
    pass


def manageInput(userInputMI):
    match userInputMI:
        case "4":
            return False
        case "1":
            acheterEssence()
        case "2":
            pass
        case "3":
            pass
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('No, Vs Code !')

    keepRefill = True
    station = StationService(6)

    while keepRefill:
        userInput = displayChoices()
        keepRefill = manageInput(userInput)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
