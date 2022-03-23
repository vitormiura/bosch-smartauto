from random import randint

def main():
    input("Diga-me sua duvida que responderei com sim ou não: ")
    if (randint(0, 1) == 0):
        print("não")
    else:
        print("sim")     
main()

