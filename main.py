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
        print("____________________________________________________________________________________________")
        print("|                                                                                           |")
        print("| Welcome to Phrase Encryption. Here you can encrypt messages in the algorythm you want.    |")
        print("|                             Just choose the option you want here.                         |")
        print("| Choose an option:                                                                         |")
        print("| 1-Encrypt to numbers                                                                      |")
        print("| 13-Encrypt to ROT13                                                                       |")
        print("| 18-Encrypt to ROT18                                                                       |")
        print("| 47-Encrypt to ROT47                                                                       |")
        print("| ...                                                                                       |")
        print("| 99-Exit.                                                                                  |")
        print("|___________________________________________________________________________________________|")
    
        option = int(input(""))

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
        
        elif option == 99:
            exitingScreen()
            exited = True

if __name__ == "__main__":
    menu()