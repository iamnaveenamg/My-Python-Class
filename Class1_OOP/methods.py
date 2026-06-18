class myClass:
    my_var=100

    # dunder methosd or magic method
    def __init__(self):
        print("This is the constructor Method")

    def __str__(self):
        return "This is string representation of the object"

    @classmethod
    def change_value(self, new_value):
        myClass.my_var=new_value

    @staticmethod
    def dummy():
        print("This is a dummy method")

obj1=myClass()
obj1.my_var= 200
print(obj1.my_var) #200

obj2=myClass()
print(obj2.my_var) #100

obj3=myClass()
print(obj3.dummy())  ## this is dummy method

obj4=myClass()
print(obj4)  # It will what ever present in the __init__ and __str__ methods