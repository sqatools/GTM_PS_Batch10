def Arithmetic(a,b,c,d):
    try:
        sum=a+b
        print(sum,":sum")
        try:
            div=c/d
            print(div,"div")
        except Exception as d:
            print("Inner exception:",d)
    except Exception as f:
        print("outer exception:",f)

    else:
        print("Multiple Except Blocks executed successfully")
    finally:
        print("finally block exeecuted")

Arithmetic(12,'hi',3,0)