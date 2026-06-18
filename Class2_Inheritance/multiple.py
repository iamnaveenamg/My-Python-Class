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

    def info(self):

        response=Company.info(self)
        print(f"The Employee: {self.employee_name} ,{response}")

class Contractor(Company):
    def __init__(self, contractor_name:str,company_name:str):
        self.contractor_name:str=contractor_name
        self.company_name:str=company_name

    def info(self):
        response1=Company.info(self)
        print(f"The Contractor: {self.contractor_name} ,{response1}")

     
com_obj=Employee("Naveen", "Tech Solutions")
com_obj.info()

contractor_obj=Contractor("Praveen", "Tech Solutions")
contractor_obj.info()