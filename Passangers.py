from People import *


class Passangers(People):

    def __init__(self, fname, lname, dob, email, passport_number):
        super().__init__(fname, lname, dob, email)
        self.__passport_number = passport_number

    def show(self):
        return (
            f'Full name {self.firstname} {self.lastname}, E:mail: {self.email} Date of Birth: {self.dob} Passport Number: {self.__passport_number}')


        