"""
Class : Class is the blueprint of the object, where we define all the methods, variables, attributes
        and property.

Object : Object is entity through which we can access the property of class.

Method : When we define any function inside the class then it is called method.

        There are three types of methods in class
        1. Instance method : When we define any method with self as first parameter, then it is called
                            as instance method.
            e.g.
                def addition_values(self, num1, num2):
                    print("Addition :", num1 + num2)

        2. Class method : When we define any method with @classmethod decorator ans cls as first
                        parameter then it is called as class method.
            e.g.
                @classmethod
                def show_city_name(cls):
                    print(cls.city)

        3. Static method : When we create a method with decorator as @staticmethod then it is called
                            as static method.
                            Static methods are associated with class name, no need to create object
                            of the class to call the static method.
            e.g.
                @staticmethod
                def factorial(var1)
                    code

Variable : When we define any variable inside the class, then it called as class member variable.

            There are two types of variables inside the class.
            1. Class variable / static variable : If we define any variable on class level then it is
                                called as class variable.
                e.g.
                class xyz:
                        city = "Mumbai"
                        country = "India"

            2. Instance variable : When we define any variable with the self keyword then it is
                                    called as instance variable.
                e.g.
                    self.v_1 = v1
                    self.v_2 = v2

constructor : Constructor that initialize the memory of the object of the class.
            By default, constructor will be called internally, whenever will create object of the
            class.

            There are two types of constructor
            1. Default Constructor : Default Constructor will be called, initially whenever we create
                                    object of the class.

                def __init__(self)
                    code

            2. Parametrize Constructor : When we pass parameter to the constructor, then it is called
                                        as parametrized constructor.
                def __init__(self, v1, v2)
                    self.v_1 = v1
                    self.v_2 = v2

Self : Self is nothing but object / instance of the class itself.
    Whenever we call any instance method with the object, then no need to pass any value for self
    parameter, as object itself is considered as first parameter of the method internally.
"""


class ABC:
    city = "Mumbai"  # Class variable / static variable
    country = "India"  # Class variable / static variable


    def __init__(self, v1, v2):
        """
        v1, v2 are two constructor parameter, the value for v1, v2 will provide during the
        creation of class.
        If we want to access the values of v1 and v2, then we have to create two separate instance
        variable self.v_1 and self.v_2

        :param v1: This is  constructor parameter v1
        :param v2: This is constructor parameter v2
        """
        print("---Welcome to OOPS concept---")
        self.v_1 = v1 # instance variable
        self.v_2 = v2 # instance variable

        self.print_table()

    def greeting(self):  # instance method
        print("Hello Good Morning")

    def print_table(self, num=5): # instance method
        for i in range(1, 11):
            print(i, "*", num, "=", i*num)

    def addition_values(self): # instance method
        print("Addition :", self.v_1 + self.v_2)

    def multiplication(self, num1, num2): # instance method
        print("multiplication output :", num1*num2)

    @classmethod
    def show_city_name(cls):
        print("City name :", cls.city)

    @staticmethod
    def factorial(num):
        """
        Static method is just like normal function outside the class. This method directly  associated
        with class name, no need to create object of the class to access the static method.
        We can directly access static method with class name.

        :param num:
        :return:
        """
        fact = 1
        for i in range(5, 0, -1):
            fact = fact*i
        print(f"Factorial of {num} :", fact)
# create object of the class
obj = ABC(50, 60)
# access method through object
obj.greeting()
obj.addition_values()
obj.multiplication(7, 10)

print("-"*50)
# access class method with class name
ABC.show_city_name()

print("-"*50)
# access static method with class object
obj.factorial(7)


print("-"*50)
# access static method with class name
ABC.factorial(5)


print("-"*50)
# can not access instance method with class name
# ABC.greeting()
# TypeError: ABC.greeting() missing 1 required positional argument: 'self'


# Homework
# create a class with name Car, with parameters car_name, car_price, car_comp
# create all different types of methods.
# create all types of variables
# create a parameterized constructor.


print("-"*50)
# call method with object
obj.greeting()  # call method with object

ABC.greeting(obj)  # call method with class name, then we have pass object parameter to the method.
# TypeError: ABC.greeting() missing 1 required positional argument: 'self'
