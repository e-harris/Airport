from aircraft_class import *

class Helicopter(Aircraft):
    def __init__(self, cargo, number_of_blades):
        super().__init__(cargo)
        self.number_of_blades = number_of_blades


def create_helicopter():
    while True:
        print("Creating helicopter")
        ask1 = input("How many blades does the helicopter have? \n"
                     "> "
                     )
        ask2 = input("What is the helicopter carrying? \n"
                     "> ")
        helicopter = Helicopter(ask2, ask1)
        print(f"Helicopter with {helicopter.number_of_blades} blades carrying {helicopter.cargo} has been created.")
        ask3 = input("Make another helicopter? Y/N \n"
                     "> ")
        if ask3.upper() == "N":
            break
