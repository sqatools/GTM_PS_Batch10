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
        ->  wheneve we call any instance method with the object, then no need to pass any value for self parameter, as object
            itself is consider as first parameter of the method internally.


"""


class ABC:

    city = "Mumbai"  # class variable/ static variable
    country = "India" # class variable/ static variable

    def __init__(self, v1, v2):
        """
        v1, v2 are two constructor parameter, the value for v1 and v2 will provide
        during the creation of object of the class.
        If we want to access the values v1 and v2, then we have to create two separate
        instance variable self.v_1 and self.v_2

        :param v1: This is constructor parameter 1
        :param v2: This is constructor parameter 2
        """
        print("--- Welcome to OOPS concepts ----")
        self.v_1 = v1  # instance variable
        self.v_2 = v2  # instance variable

        self.print_table()

    # instance method
    def greeting(self):
        print("Hello Good Morning")

    def print_table(self, num=5):   # instance method
        for i in range(1, 11):
            print(i, "*", num, "=", i * num)

    def addition_values(self):  # instance method
        print("addition :", self.v_1 + self.v_2)

    def multiplication(self, num1, num2):  # instance method
        print("multiply output :", num1*num2)

    @classmethod
    def show_city_name(cls):
        print("city name :", cls.city)

    @staticmethod
    def factorial(num): #  static method
        """
        static methods are just like normal function outside of the class, this method directly associated
        with class name, no need to create object of the class to access the static method.
        we can directly access static method with class name.

        :param num:
        :return:
        """
        fact = 1
        for i in range(5, 0, -1):
            fact = fact*i

        print(f"Factorials of {num} :", fact)


# create object of the class
obj = ABC(50, 60)
# access method through object
obj.greeting()
obj.addition_values()
obj.multiplication(7, 8)

print("_"*24)
# access static method will class object
obj.factorial(7) # Factorials of 7 : 120

print("_"*24)
# access static method with class name
ABC.factorial(5) # Factorials of 5 : 120

print("_"*24)
# access class method with class name
ABC.show_city_name() # city name : Mumbai

print("_"*24)
# can not access instance method with class name
# ABC.greeting()
# TypeError: ABC.greeting() missing 1 required positional argument: 'self'

#####################
# Home work
# create a class with name Car, with parameters car_name, car_price, car_comp
# create all different types of methods.
# create all types of variables
# create a parametrize constructor.

print("_"*24)
###########################################
# call method with object

obj.greeting() # calling method with object
ABC.greeting(obj) # call method class name, then we have pass object as parameter to the method.