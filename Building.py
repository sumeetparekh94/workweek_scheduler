from Building_Type import Building_Type
import copy

class Building(object):
    """
    Class for building which includes the following attributes.
    - id: building id
    - type: buidling type (from Building_Type enum)
    - is_complete: flag to check if installation on building is complete
    - building_dict: data structure to handle constraints where different buildings require 
      a specific count of different types to employees to complete the task
    - emp_list = revert to original count if task does not complete
    """
    
    def __init__(self,id,type):
        self.id = id
        self.type = type.value
        self.is_complete = False
        self.building_dict = {"1" :[[[1], 1]], "2" : [[[1], 1], [[2, 3],1]], "3" : [[[1], 2], [[2], 2], [[1,2,3],4]]}
        self.emp_list = copy.deepcopy(self.building_dict[str(self.type)])
