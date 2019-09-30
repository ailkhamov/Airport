from People import *

class Staff(People):
    
    def __init__(self,staffid, fname,lname,dob, email, role):
        super().__init__(fname,lname,dob, email)
        self.staffid = staffid
        self.role = role
        

    def show(self):
        return ([f' Staff id: {self.staffid} Full name {self.firstname} {self.lastname}, E:mail: {self.email} Date of Birth: {self.dob} Role: {self.role}'])
    
    