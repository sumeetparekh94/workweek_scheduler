from Building_Type import Building_Type
import copy

class Building(object):
    
    def __init__(self,id,type):
        self.id = id
        self.type = type.value
        self.is_complete = False
        self.building_dict = {"1" :[[[1], 1]], "2" : [[[1], 1], [[2, 3],1]], "3" : [[[1], 2], [[2], 2], [[1,2,3],4]]}
        self.emp_list = copy.deepcopy(self.building_dict[str(self.type)])
