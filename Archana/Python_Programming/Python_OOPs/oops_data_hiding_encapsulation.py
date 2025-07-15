
"""
Data hiding can be achieved when we defined any variable/method with single underscore or double underscore as prefix


"""
class Car:
    def __init__(self, car_name, car_comp, car_price):
        self.car_name = car_name
        self._car_company = car_comp
        self.__car_price = car_price

    def show_car_name(self):
        print("car name :", self.car_name)

    def _show_car_company(self):
        print("car company :", self._car_company)

    def __show_car_price(self):
        print("car price :", self.__car_price)


obj = Car("Harier", "TATA", "20 Lac")

# 1.  when we define any variable/method with single/double underscore as prefix, then those variable/method will not visible
# in suggestion list
obj.show_car_name()

# access single under prefix data member
obj._show_car_company()

# access any variable/method with double underscore as prefix
obj._Car__show_car_price()

print(dir(obj))

#obj.__show_car_price()
