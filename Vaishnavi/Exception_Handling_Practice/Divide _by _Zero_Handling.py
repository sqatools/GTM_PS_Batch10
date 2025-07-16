#1. Divide by Zero Handling
def div_zero(n1,n2):
    try:
        div=n1//n2
        print(div,"division on no")
    except Exception as e:
        print("error:",e)
    else:
        print("Execution successful")

div_zero(23,2)
