class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def get_info(self):
        return "Name: {}, Id: {}".format(self.name,self.id)
class Manager:
    def __init__(self,department):
        self.department=department
    def manage_project(self):
        return "Department: {}".format(self.department)
class Technician:
    def __init(self,specialization):
        self.specialization=specialization
    def perform_maintenance(self):
        return "Specialization: {}".format(self.specialization)
class TechManager(Manager,Technician):
    def __init__(self,name,id,department,specialization):
        super().__init__(name,id,department,specialization)
        self.team=[]
    def add_employee(self,data):
        self.team.append(data)
    def get_info(self):
        return "Name: {}, Id: {},Department: {}, Specialization: {}".format(self.name,self.id,self.department,self.specialization)
    def get_team_info(self):
        result=""
        for joiner in self.team:
            result+=f'{joiner.get_info()}'
        return result


