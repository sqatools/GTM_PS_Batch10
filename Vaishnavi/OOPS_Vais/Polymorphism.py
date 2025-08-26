class XYZ:
    def greeting(self):
        print("---XYZ---")
        print("Good morning")

    def string_mul(self,str,num):
        print(str*num)

class ABC(XYZ):

    def greeting(self):
        print("---ABC----")
        print("Good morning")

    def addition(self,n1,n2,n3):
        print("Sum :",n1+n2+n3)

    def addition(self,n1,n2):
        print("Sum :", n1 + n2)

obj=ABC()
obj.greeting()
obj.addition(12,11)




