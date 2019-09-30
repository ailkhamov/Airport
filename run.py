from Flight import *
from Passangers import *
from People import *
from Staff import *

# Flight Objects Implemented 
flight_1 = Flight(1,"England","UK")
flight_2 = Flight(2,"Romania","UK")
flight_3 = Flight(3,"Portugal","Brazil")

# Passagers for flight 1
passanger1 = Passangers("Abror", "Ilkhamov",1994-5-12,"ilkhamovab@gmail.com",123456)
passanger2 = Passangers("Olsi", "Berisha", 1994-4-12,"olsi_b@gmail.com", 122151)
passanger3 = Passangers("Nick", "Levenitis",3-5-1994,"ilkhamovab@gmail.com", 1501)

# Appending Passangers objects into flight's passanger list attribute
flight_1.add_passanger(Passangers.show(passanger1))
flight_1.add_passanger(Passangers.show(passanger2))
flight_1.add_passanger(Passangers.show(passanger3))

#passangers for flight 2
passanger4 = Passangers("Andrea", "Anderson", 1994-5-21, "andrea@gmail.com",11251)
passanger5 = Passangers("Silva", "Kun", 4-5-1994, "silvia@gmail.com", 1215532)
passanger6 = Passangers("Akvile", "Dov", 12-11-85, "akvile@gmail.com", 12124015)

# Appending Passengers into flight 2
flight_2.add_passanger(Passangers.show(passanger4))
flight_2.add_passanger(Passangers.show(passanger5))
flight_2.add_passanger(Passangers.show(passanger6))

#Passangers for flight 3
passanger7 = Passangers("Odil","Ilhaamov", 11-5-76, "odil@gmail.com", 112001)
passanger8 = Passangers("Aziz", "Muhamedov", 5-5-53, "aziz@gmail.com", 12501)
passanger9 = Passangers("Maggi", "Magdela", 11-11-92, "maggi@gmail.com",121421)

#Appending Passangers into Flight 3
flight_3.add_passanger(Passangers.show(passanger7))
flight_3.add_passanger(Passangers.show(passanger8))
flight_3.add_passanger(Passangers.show(passanger9))

# Creating Staff
staff_1 = Staff(1,"Jack","Thompas",12-5-1989,"jack@gmail.com", "Cabin crew")
staff_2 = Staff(2, "Emily","Nelson", 15-12-1924, "emily@gmail.com","Cabin crew")
staff_3 = Staff(3, "Thomas", "Durak", 15-12-1921, "thomas@gmail.com", "Captain")
staff_4 = Staff(4, "Wayne", "Rooney", 21-12-1959, "rooney@gmail.com", "Cabin Crew")
staff_5 = Staff(5, "Didier", "Drogba", 21-51-1951, "drogba@gmail.com", "Captain")

# Appending Staff into flight 1
flight_1.add_staff(Staff.show(staff_1))
flight_1.add_staff(Staff.show(staff_2))
flight_1.add_staff(Staff.show(staff_3))

# Appending staff into Flight 2
flight_2.add_staff(Staff.show(staff_4))
flight_2.add_staff(Staff.show(staff_5))




# flight1 = [flight_1]
# flight2 = [flight_2]
# flight3 = [flight_3]

print(flight_1.flight_number,flight_1.origin)

print("Welcome to Heathrow Airport database! ")
print("Please choose of the following options:")
print("Select Option 1 if you would like to List All Available flights ")
print("Select Option 2 if you would like to List All Passengers in the selected flights")
print("Select Option 3 if you would like to remove passanger from the Flight List")


choice = int(input("Enter your choice"))


while True:
    if choice == 1:
        print(Flight.flightshow(flight_1))
        print(Flight.flightshow(flight_2))
        print(Flight.flightshow(flight_3))

        choice = int(input("Enter choice again:"))
        
    elif choice == 2:
        p_choice = int(input("Select the flight number you wish to see all the staff/passangers"))
        if p_choice == 1:
            print("Passangers List:")
            print(*Flight.getPassengerList(flight_1), sep="\n")
            print("Staff List: ")
            print(*Flight.getStaffList(flight_1), sep = "\n")
            
            choice = int(input("Enter choice again:"))
        elif p_choice == 2:
            print("Passangers List:")
            print(*Flight.getPassengerList(flight_2), sep = "\n")
            print("Staff List:")
            print(*Flight.getStaffList(flight_2), sep = "\n")
            if True:
                choice = int(input("Enter choice again:"))

        elif p_choice == 3:
            print("Passangers List:")
            print(*Flight.getPassengerList(flight_3), sep ="\n")
            print("Staff List: ")
            print(*Flight.getStaffList(flight_3), sep = "\n")
            if True:
                choice = int(input("Enter choice again:"))
        else:
            print("You have chosen the wrong number")
            if True:
                p_choice = int(input("Enter choice again"))
    elif choice == 3:
        choose_flight = int(input("Which flight would you like a remove passenger from?: "))
        del_passanger = input("Which passanger would you like to delete?:")
        if choose_flight == flight_1.getFlight_no():
            flight_1.removePassanger(del_passanger)
            if True:
                choice = int(input("Enter choice again:"))
        elif choose_flight == flight_2.getFlight_no():
            flight_2.removePassanger(del_passanger)
            if True:
                choice = int(input("Enter choice again:"))

        elif choose_flight == flight_3.getFlight_no():
            flight_3.removePassanger(del_passanger)
            if True:
                choice = int(input("Enter choice again:"))
        
    # elif choice ==4:
    #     choose_flight = int(input("Which flight would you like a modify passenger from?: "))
    #     passanger = input("Enter the passanger's detail you with to modify")
    #     new_detail = input("Enter your new information: ")
    #     if choose_flight == 1:
    #         flight_1.modifyPassanger(passanger,new_detail)
    #         if True:
    #             choice = int(input("Enter choice again:"))
    #









    else:
        print("You have chosen the wrong choice!")
        if True:
            choice = int(input("enter your choice again:"))





# # for flight in flight1:
#     passengers = flight.getPassengerList()
#     print("Flight1:")
#     for passanger in passengers:
#         print(passanger.show())
#








