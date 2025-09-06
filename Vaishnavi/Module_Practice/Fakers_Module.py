from faker import Faker

fk=Faker()
n=int(input("Enter the range"))
count=1
for i in range(1,n+1,1):
    Name=fk.name()
    User_Name=fk.user_name()
    Mobile_No=fk.phone_number()
    Date= fk.date()

    print("Name:",Name)
    print("User_Name:", User_Name)
    print("Mobile_No:", Mobile_No)
    print("Date:", Date)

    with open("Faker.txt","a") as f:
        data=f"{count} : {Name} {User_Name} {Mobile_No} {Date}\n"
        f.write(data)
        count+=1
        print("_"*50+"\n")


"""
1.Excel File handling
2.OS Modules-OS,sqllite
3.OOPS concept
4.Data conversions
"""