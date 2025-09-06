class Car:
    def __init__(self,car_name,car_price,Car_Company):
        self.car_name=car_name
        self._car_price=car_price
        self.__Car_Company=Car_Company

    def Show_Car_Name(self):
        print("car name",self.car_name)

    def _show_car_price(self):
        print("car price:",self._car_price)

    def __show_car_company(self):
        print("car company:",self.__Car_Company)

obj=Car("Harrier","12 lacs","TATA")

obj.Show_Car_Name()
obj._show_car_price()
obj._Car__show_car_company()