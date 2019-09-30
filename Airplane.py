class Airplane:

    def __init__(self,brand,airline):
        self.brand = brand
        self.airline = airline
        self.airplane_list = []
        self.airplane_count = len(self.airplane_list)

    def addAirlineList(self, airplane):
        self.airline_list.append(airplane)


    def show(self):
        return (f' Brand: {self.brand}, Airline: {self.airline} Number of airplanes: {self.airplane_count}')
