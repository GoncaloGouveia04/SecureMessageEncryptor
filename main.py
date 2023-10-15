from library import *

def exitingScreen():
    print("Exiting...")
    print("Goodbye.")

def chooseIfExiting(option2):
    while option2 != "yes" and option2 != "no":
        option2 = input("Do you wish to continue(yes or no)? ")
        if option2 == "yes":
            return False
        else:
            exitingScreen()
            return True

def menu():
    exited = False
    while not exited:
        print("-" * 80)
        print("|{:^78}|".format("Welcome to Phrase Encryption"))
        print("|{:^78}|".format("Here you can encrypt messages using various algorithms."))
        print("-" * 80)
        print("|{:<3} Encrypt to numbers (1) {:<51}|".format("", ""))
        print("|{:<3} Encrypt to ROT13 (13){:<53}|".format("", ""))
        print("|{:<3} Encrypt to ROT18 (18){:<53}|".format("", ""))
        print("|{:<3} Encrypt to ROT47 (47){:<53}|".format("", ""))
        print("|{:<3} ...                      {:<49}|".format("", ""))
        print("|{:<3} Exit (99)                {:<49}|".format("", ""))
        print("-" * 80)
    
        option = int(input("Choose an option from the menu: "))

        if option == 1:
            phrase = input("Insert the phrase or word you want to encrypt to numbers: ")
            print(translateToNumbers(phrase))
            option2 = ""
            exited = chooseIfExiting(option2)
        elif option == 13:
            phrase = input("Insert the phrase or word you want to encrypt to ROT13: ")
            print(translateToROT13(phrase))
            option2 = ""
            exited = chooseIfExiting(option2)
        elif option == 18:
            phrase = input("Insert the phrase or word you want to encrypt to ROT18: ")
            print(translateToROT18(phrase))
            option2 = ""
            exited = chooseIfExiting(option2)
        elif option == 47:
            phrase = input("Insert the phrase or word you want to encrypt to ROT47: ")
            print(translateToROT47(phrase))
            option2 = ""
            exited = chooseIfExiting(option2)
        
        elif option == 99:
            exitingScreen()
            exited = True

if __name__ == "__main__":
    menu()