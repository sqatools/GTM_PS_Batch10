class ABC:
    city="Mumbai"
    Country="India"

    @classmethod
    def show_city_name(cls):
        print(cls.city)
        print(cls.Country)

    @staticmethod
    def factorial(num):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print("factorrial of num is",fact)

obj=ABC()
obj.show_city_name()
obj.factorial(5)
ABC.factorial(7)