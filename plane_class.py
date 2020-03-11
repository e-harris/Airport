from aircraft_class import *
# define plane class
# it inherits from aircraft

# attributes it needs:
    # plane_number


# Plane
# As a User I can create a Plane with a plane number


class Plane(Aircraft):
    def __init__(self, cargo, plane_number):
        super().__init__(cargo)
        self.plane_number = plane_number



def create_plane():
    while True:
        print("Creating plane")
        ask1 = input("What is the code of the plane? \n"
                     "> "
                     )
        ask2 = input("What is the plane carrying? \n"
                     "> ")
        plane = Plane(ask1, ask2)
        print(f"Plane {plane.plane_number} carrying {plane.cargo} has been created.")
        ask3 = input("Make another plane? Y/N \n"
                     "> ")
        if ask3.upper() == "N":
            break
