from availability import Availability

class Employee(object):
    
    def __init__(self,id,type,availability):
        self.id  = id
        self.availability = Availability(availability)
        self.type = type
    
    
    def isAvailable(self, day_of_week):
        return self.availability.week[day_of_week]