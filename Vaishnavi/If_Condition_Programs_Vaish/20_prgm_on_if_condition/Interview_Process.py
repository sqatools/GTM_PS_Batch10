#Python program to describe the interview process.

Round1= "pass"
Round2 = "pass"
Round3 ="fail"

if Round1=="pass":
    print("1st round cleared")
    if Round2=="pass":
        print("2nd round is cleared")
        if Round3 =="pass":
            print("3rd round is cleared")
        else:
            print("Sorry! You didn't pass the interview")

    else:
        print("2nd round is not cleared")
else:
    print("1st round not cleared")