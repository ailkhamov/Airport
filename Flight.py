from Passangers import *
class Flight():

    def __init__(self, flight_no,destination,origin):
        self.flight_number = flight_no
        self.destination = destination
        self.origin = origin
        self.passanger_list = []
        self.stafflist = []
    
    def printAllPassangers(self, flight):
        for self.passanger_list in flight:
            for passanger in self.passanger_list:
                print(passanger.show())

    def add_passanger(self, passenger):
        self.passanger_list.append(passenger)
    
    def add_staff(self, staff):
        self.stafflist.append(staff)
    
    def getStaffList(self):
        return self.stafflist

    # def flight_list(self, flight):
    #     self.flight.create_passanger_list()

    def getFlight_no(self):
        return self.flight_number
    
    def getDestination(self):
        return self.destination
    
    def getOrgin(self):
        return self.origin

    def getPassengerList(self):
         return self.passanger_list
    
    def returnPassengerList(self):
        return self.add_passanger()
    

    def flightshow(self):
        return (f'"Flight number: {self.flight_number} Destination: {self.destination} Origin: {self.origin}')
    
    def removePassanger(self,passanger):
        for passanger in self.passanger_list:
            self.passanger_list.remove(passanger)
        return self.passanger_list

    def modifyPassanger(self, passanger, newpass):
        for i, item in enumerate(self.passanger_list):
            if passanger in item:
                self.passanger_list = newpass
        return self.passanger_list

    
    
    
    
        
        