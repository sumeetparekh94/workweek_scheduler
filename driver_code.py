from Employee import Employee
from Building import Building
from Building_Type import Building_Type
from pprint import pprint


class WorkweekScheduler(object):
    
    def schedule(self, buildings, employees):
        """
        Method containing the main logic for creating the schedule. The approach follows a greedy approach based on the order in which
        the list of buildings is provided since that is the order of importance.
        
        We define a 2d matrix where the columns are the days of the week and each row is an employee. The values in the grid would be the
        id of the building the employee would be working on a specific day.
        
        Args:
            buildings ([list]): list of buildings that employees have to work on
            employees ([list]): list of employees

        Returns:
            [[list]]: returns the workweek schedule in the form of a 2d matrix
        """
        
        # initialize the 2d matrix
        workweek = [[ 0 for _ in range(5)] for _ in range(len(employees))]
        
        # fill the grid with -1 initially
        for i in range(len(workweek)):
            for j in range(len(workweek[0])):
                if not employees[i].isAvailable(j):
                    workweek[i][j] = -1
        
        # greedy approach to update the grid
        for i in range(5):
            for j in range(len(buildings)):
                    employee_ids = []
                    if not buildings[j].is_complete:
                        for k in range(len(employees)):
                            if workweek[k][i] != 0 or workweek[k][i] == -1:
                                continue
                            else:
                                if self.needEmployee(buildings[j],employees[k]):
                                    employee_ids.append(k)
                        self.update_building(buildings[j],employee_ids)
                        if buildings[j].is_complete == True:
                            workweek = self.updateWorkWeek(employee_ids,buildings[j].id,i,workweek)
                        else:
                            self.revert(buildings[j])
                            
        return workweek
                    
                                    
                                
    def updateWorkWeek(self, emp_ids, building_id, day,workweek):
        """
        Method to update the workweek grid
        
        Args:
            emp_ids (int): eployee id
            building_id (int): building id
            day (string): day of the week
            workweek ([[list]]): workweek 2d grid

        Returns:
            [[list]]: updated workweek 2d grid
        """
        for i in emp_ids:
            workweek[i][day] = building_id
        return workweek

                            
    def update_building(self, building, employee_ids):
        """
        Method to update building id for a set of employees.

        Args:
            building (object): building object
            employee_ids ([list]): list of employees working on a specific building
        """
        if building.type == 1:
            if len(employee_ids) == 1:
                building.is_complete = True
        if building.type == 2:
            if len(employee_ids) == 2:
                building.is_complete = True
        if building.type == 3:
            if len(employee_ids) == 8:
                building.is_complete = True
                        
                        
    def needEmployee(self, building, employee):
        """
        Method to determine whether there is a need for the employee on a specific building.

        Args:
            building (object): building object
            employee (object): employee object

        Returns:
            boolean : true or false for the need of an employee on a particular building
        """
        
        for i in  building.emp_list:
            if employee.type in i[0] and i[1]>0:
                i[1] -= 1
                return True
            
        return False

    def revert(self, building):
        """
        Method to revert to original data structure for building dictionary since that employee was not used on the building.
        
        Args:
            building (object): building object
        """
        building.emp_list = building.building_dict[str(building.type)]


if __name__ == '__main__':
    
    # employees = [
    #     Employee(1,1,"10001")]
    # buildings = [Building(1,Building_Type.SINGLE_STORIED_HOMES)]
    # pprint(WorkweekScheduler().schedule(buildings, employees))
        # SINGLE_STORIED_HOMES = 1
        # TWO_STORIED_HOME = 2
        # COMMERCIAL = 3


    # employees = [
    #     Employee(1,1,"10001"),Employee(2,2,"10001"),Employee(3,3,"10001"),Employee(4,1,"10001"),Employee(5,1,"10001"),Employee(6,2,"10001"),Employee(7,3,"10001"),Employee(8,1,"10001")]
    # buildings = [Building(3,Building_Type.COMMERCIAL),Building(4,Building_Type.COMMERCIAL)]
    # pprint(WorkweekScheduler().schedule(buildings, employees))

    # Building(1,Building_Type.SINGLE_STORIED_HOMES),Building(2,Building_Type.TWO_STORIED_HOME),

    employees = [
        Employee(1,1,"10001"),Employee(2,2,"10001"),Employee(3,3,"10001"),Employee(4,1,"10001"),Employee(5,1,"10001"),Employee(6,2,"10001"),Employee(7,3,"10001"),Employee(8,1,"10001")]
    buildings = [Building(1,Building_Type.SINGLE_STORIED_HOMES),Building(2,Building_Type.TWO_STORIED_HOME),Building(4,Building_Type.COMMERCIAL)]
    pprint(WorkweekScheduler().schedule(buildings, employees))

    Building(1,Building_Type.SINGLE_STORIED_HOMES),Building(2,Building_Type.TWO_STORIED_HOME),
    
    WorkweekScheduler().schedule(buildings, employees)
            
        
        
                        
                        

        
