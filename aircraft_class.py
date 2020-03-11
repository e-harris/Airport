# aircraft class
# attributes: cargo

# Define a couple methods; accelerate and brake


class Aircraft:
    def __init__(self, cargo):
        self.cargo = cargo


    def accelerate(self):
        return "Go Forward"

    def brake(self):
        return "Stop moving"

