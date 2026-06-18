class Company:

    title:str="consultancy"
    
    def __init__(self, company_name:str ):
        self.company_name:str=company_name

    def info(self):
        print(f"Comapny Name: {self.company_name}")
        return f"Comapny Name: {self.company_name}"

class Employee(Company):

    def __init__(self, employee_name, company_name):
        self.employee_name=employee_name
        self.company_name=company_name

    def Employee_info(self):

        response=Company.info(self)
        print(f"The Employee: {self.employee_name} ,{response}")



com_obj=Employee("Naveen", "Tech Solutions")
com_obj.Employee_info()