class ABC:
    city="Mumbai"
    Country="India"

    @classmethod
    def show_city_name(cls):
        print(cls.city)
        print(cls.Country)

obj=ABC()
obj.show_city_name()