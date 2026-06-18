class MyClass:

    # Creation of Class Variables
    var1="Naveen"
    var2="Reddy"

    #instance variables
    def __init__(self, dyn1, dyn2, dyn3):
        self.dyn1=dyn1
        self.dyn2=dyn2
        self.dyn3=dyn3

    #Methods
    def func1(self):
        print(f"Hello World, {self.dyn1}")
    
    def func2(self):
        print(f"Hello Naveen, {self.dyn2}")
    
    def func3(self):
        print(f"Hello Naveen, {self.dyn3}")

# Create Objects
obj=MyClass('abc','xyz', 'bbb')
#obj2=MyClass()

# this Print the code inside the fun
obj.func1()
#obj2.func2()

# Another Way to call the function
MyClass.func2(obj)
obj.func3()

