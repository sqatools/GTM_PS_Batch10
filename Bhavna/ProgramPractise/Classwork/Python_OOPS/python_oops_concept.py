# 09/07/2025 Session - Absent

"""
class : Class is the blueprint of the object, where we defined all the methods, variable, attributes and property.

object : object is entity through which we can access the all properties of class.

method : When we define any function inside the class, then it is called method.
         # There are three types of method in the class
         1. Instance method: when we defined any method, with self as first parameter, then it is called instance
            method e.g.

            def addition_value(self, num1, num2)
                 print("addition:", num1+num2)

         2. class method: when we define any method with @classmethod decorator, and cls and first parameter
                          then it is called, class method. e.g.

            @classmethod
            def show_city_name(cls):
                print(cls.city)

         3. static method: when we create a method with decorator as @staticmethod, then it is called static method.
                           ->  static method are associated with class name, no need to created object of the class
                               to call the static method.

            @staticmethod
            def factorial(var1):
                code

variable : when we define any variable, inside the class, then it is class member variable.
           # There are two types of variable inside the class.
           1. class variable/static variable : If we define any variable on class level, then it is
              called class variable. e.g.
              class xyz:
                       city = "Mumbai"
                       country = "India"

           2. instance variable :  when we define any variable with the self keyword, then it is called
              instance variable. e.g.
              self.v_1 = v1
              self.v_2 = v2

constructor:  Constructor that initialize the memory of the object of the class.
            ->  By default constructor will be called internally, whenever will create object of the class.

            # There are two type of constructor
            1.  Default constructor: default constructor will be called, initially whenever we create object
                of the class.

                def __init__(self)
                    code

            2.  Parametrize constructor: When we pass parameter to the constructor, then it is called parametrize
                constructor.
                def __init__(self, v1, v2)
                    self.v_1 = v1
                    self.v_2 = v2


self :  self is nothing but object/instance of the class itself.
        ->  whenever we call any instance method with the object, then no need to pass any value for self parameter, as object
            itself is consider as first parameter of the method internally.

"""


class ABC:
    city = "Nagpur" # static variable/ class variable
    country = "India" #static variable/ class variable
    def __init__(self,v1,v2):
        """
        v1, v2 are two constructor parameter, the value for v1 and v2 will provide
        during the creation of object of the class.
        If we want to access the values v1 and v2, then we have to create two separate
        instance variable self.v_1 and self.v_2

        :param v1: This is constructor parameter 1
        :param v2: This is constructor parameter 2
        """
        print("Welcome to the course")
        self.v_1 = v1 # whenever we define a variable with self then it is "instance variable"
        self.v_2 = v2 # Instance Variable

        self.print_table()

#########instance Method########
    def greeting(self):
        print("Good Evening")

    def print_table(self, num=2):
        for i in range(1,11):
            print(i,'*',num,'=',num*i)

    def addition_values(self):
        print("Addition:",self.v_1+self.v_2)

    def multiplication(self,num1,num2):
        print("Multiply Output:",num1*num2)

    @classmethod
    def show_city_name(cls):
        print("City name:",cls.city)

    @staticmethod
    def factorial(num):  #static method
        """
                static methods are just like normal function outside of the class, this method directly associated
                with class name, no need to create object of the class to access the static method.
                we can directly access static method with class name.

                :param num:
                :return:
        """
        fact = 1
        for i in range(5,0,-1):
            fact= fact*i

        print(f"factorial of {num}:",fact)

# create object of the class
obj = ABC(50,30)
# access method through object
obj.greeting()
obj.addition_values()
obj.multiplication(7,8)
print('_'*70)
# access static method will class object
obj.factorial(7)
print('_'*70)
# access static method with class name
ABC.factorial(5)
print('_'*70)
# access class method with class name
ABC.show_city_name()
print('_'*70)
# can not access instance method with class name
# ABC.greeting()
# TypeError: ABC.greeting() missing 1 required positional argument: 'self'

print('_'*70)

########################################

# Home work
# create a class with name Car, with parameters car_name, car_price, car_comp
# create all different types of methods.
# create all types of variables
# create a parametrize constructor.

class Car:

    city1 = "Pune"

    def __init__(self,c1,c2,c3):
        print("welcome to showroom")
        self.car_name = c1
        self.car_price = c2
        self.car_comp = c3

    def show_car_name(self):
        print("Car Name:",self.car_name)

    def show_car_price(self):
        print("Car_price:",self.car_price)

obj1 = Car('Ertiga',1500000,'BMW')

obj1.show_car_name()
obj1.car_price()