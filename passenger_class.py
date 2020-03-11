from people_class import *
# Passenger class
# inherits from people

# attributes:
# passport number


# Passengers
# as a user I can create a Passanger
# It can be created with name and passport number
# I can create 'Joana Thomson' with the Passport number 'B343123'
# I can create 'Birt Kuman' with the Passport number 'B13927'



class Passengers(People):
    def __init__(self, first_name, last_name, passport_number):
        super().__init__(first_name, last_name)
        self.passport_number = passport_number



def create_passenger():
    while True:
        print("Creating new passenger")
        first_name = input("What is the passengers first name? \n"
                     "> ")
        last_name = input(f"What is {first_name}'s last name? \n"
                     f"> ")
        full_name = first_name + last_name
        passport = input(f"What is the passport number for {full_name}: \n"
                         f"> ")
        passenger = Passengers(first_name, last_name, passport)
        print(f"Passenger {full_name}: {passenger.passport_number} created.")
        ask1 = input("Would you like to add another passenger? Y/N \n"
                     "> ")
        if ask1 == "N":
            break
