from plane_class import *
from helicopter_class import *
from people_class import *
from passenger_class import *
from flight_trip_class import *
from aircraft_class import *

# do the simplest SIMPLEST

# switch board
def switchboard():
    while True:
        print("Press 1 to create plane \n"
              "Press 2 to create helicopter \n"
              "Press 3 to create passenger \n"
              "Press 4 to create a new flight \n"
              "Press 0 to exit")
        ask1 = input("> ")
        if ask1 == "1":
            create_plane()
        elif ask1 == "2":
            create_helicopter()
        elif ask1 == "3":
            create_passenger()
        elif ask1 == "4":
            flight_book()
        elif ask1 == "0":
            break

switchboard()