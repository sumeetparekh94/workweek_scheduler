class Availability(object):
    """
    To define availability string for employee working from Monday through Friday.
    """
    
    def __init__(self,availability_string):
        
        self.week = {0 : False,1 : False ,2 : False,3: False, 4 : False}
        
        days = [k for k in availability_string]
        if len(availability_string) == 5:
            if days[0] == "1":
                self.week[0] = True
            if days[1] == "1":
                self.week[1] = True
            if days[2] == "1":
                self.week[2] = True
            if days[3] == "1":
                self.week[3] = True
            if days[4] == "1":
                self.week[4] = True
        
            
            
                    
        
        