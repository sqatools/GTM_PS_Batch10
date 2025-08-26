from faker import Faker


count =1
fk = Faker()
for i in range(1,20,1):
    namea = fk.first_name()
    print(namea)
    last_name =fk.last_name()
    print(last_name)
    city = fk.city()
    print(city)
    phone_num = fk.phone_number()
    print(phone_num)
    state = fk.state()
    print(state)
    country = fk.country()
    print(country)


