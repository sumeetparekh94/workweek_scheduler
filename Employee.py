from availability import Availability

class Employee(object):
    """
    Class for employee which has the following attributes.
    - id: employee id
    - availability: availability string for an employee who is going to work Monday through Friday
    - type: employee type (from Employee_Type enum)
    """
    
    def __init__(self,id,type,availability):
        self.id  = id
        self.availability = Availability(availability)
        self.type = type
    
    
    def isAvailable(self, day_of_week):
        return self.availability.week[day_of_week]