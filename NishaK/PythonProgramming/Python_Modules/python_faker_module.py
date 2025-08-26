from faker import Faker


fk = Faker()

for i in range(1, 50):
    print(i)
    user_name = fk.user_name()
    email = fk.email()
    phone_number = fk.phone_number()
    address = fk.address()

    print("Username :", user_name)
    print("Email :", email)
    print("Phone Number :", phone_number)
    print("Address :", address)

    with open("user_data.txt", "a") as file:
        user_details = f"{user_name}, {email}, {phone_number}, {address}\n"
        file.write(user_details)
        file.write("-"*50+"\n")
