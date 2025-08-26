

###########################################################################
round3 = input("Enter round3 result:")
round4 = input("Enter round4 result:")

if round3 == "passed":
    print("Congrats your 1st round is clear")
    if round4 == "passed":
         print("Congrats 2nd round is clear, you are placed")
    else:
        print("Failed in 2nd round, please try next time")
else:
    print("Failed in 1st round, please try next time")