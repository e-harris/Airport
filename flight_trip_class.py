#Flight Trip class

# origin
# Destination
# list of passengers
# plane number

# need some getters nd setter:

# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin

# As a user I can add a Passenger to the list of passengers


# Flight_trip
# As a user I can create a flight with no specific information
# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin
# As a user I can add a Passanger to the list of passangers
# Passanger list is a list of objct that are Passanger



class Flight_Trip():
    def __init__(self, destination, plane_number, origin = "Southend",  passengers = []):
        self.__origin = origin
        self.__destination = destination
        self.__plane_number = plane_number
        self.passengers = passengers

    # Getters

    def get__origin(self):
        return self.__origin

    def get__destination(self):
        return self.__destination

    def get_plane_number(self):
        return self.__plane_number


def flight_book():
    while True:
        print("Setting up new flight")
        ask1 = input("What is the destination? \n"
                     "> ")
        ask2 = input("What plane is being used? \n"
                     "> ")
        flight = Flight_Trip(ask1, ask2)
        print(f"Flight {flight.get_plane_number()}: {flight.get__origin()} to "
              f"{flight.get__destination()}")
        print(f"Flight {flight.get_plane_number()} successfully booked")
        print("Press 'Q' to stop adding passengers")
        while True:
            ask3 = input(f"Add passenger to flight {flight.get_plane_number()}:"
                     f"> ")
            if ask3.upper() == "Q":
                break
            flight.passengers.append(ask3)
        print(f"{flight.get_plane_number()} to {flight.get__destination()} from {flight.get__origin()}"
              f"has {len(flight.passengers)} passengers who are {flight.passengers}")
        ask4 = input("Book another flight? Y/N\n"
                     "> ")
        if ask4.upper == "N":
            break

flight_book()