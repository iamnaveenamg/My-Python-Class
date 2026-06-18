class MyClass:

    # Creation of Class Variables
    var1="Naveen"
    var2="Reddy"

    #instance variables
    def __init__(self, dyn1, dyn2, dyn3):
        self.dyn1=dyn1 # public Variables
        self.__dyn2=dyn2 # Private Variable
        self._dyn3=dyn3 # Protected Variable

    #Methods
    def func1(self):
        print(f"Hello World, {self.dyn1}")
    
    def func2(self):
        print(f"Hello Naveen, {self.__dyn2}")
    
    def func3(self):
        print(f"Hello Naveen, {self._dyn3}")

# Create Objects
obj=MyClass('abc','xyz', 'bbb')
#obj2=MyClass()
obj.dyn1='Naveen'

obj.dyn2='Reddy'
print(obj.dyn2) # # This will not give error but it will create a new variable dyn2 in the object and assign the value "stu" to it. It will not change the value of __dyn2 which is a private variable.

obj.func1()
obj.func2() # It will only private value not public value
#obj2.func2()

obj.dyn3="MG"
print(obj.dyn3)
obj.func3()


print(obj._dyn3) #  It will print "xyz" because _dyn3 is a protected variable and it can be accessed outside the class but it is not recommended to do so. It is just a convention to use _ before the variable name to indicate that it is a protected variable and it should not be accessed outside the class

# Another Way to call the function
#MyClass.func2(obj)
#obj.func3()

