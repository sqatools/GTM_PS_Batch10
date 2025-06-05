#Python program to check given number is divided by 3 or not.

# num1 = 14 #This line initializes a variable named num1 with the integer value 14.

# if num1%3 == 0:
#     print("number is divided by 3:",num1,type(num1))
# else:
#     print("check number is not divide by 3:",num1,type(num1))

    #note calculates the remainder when num1 (which is 14) is divided by 3. 14÷3=4 with a remainder of 2.
    #So, num1 % 3 evaluates to 2.
    #2 == 0 is False.
    #else:: Since the if condition is False, the code inside the else block is executed.


#If else program to get all the numbers divided by 3 from 1 to 30.


#for i in range (1,31):#This loop goes through each number i starting from 1 up to (but not including) 31. So, it checks numbers from 1 to 30.
#    if i%3 == 0: # Inside the loop, this condition checks if the current number i is perfectly divisible by 3. The modulo operator (%) returns the remainder of a division. If the remainder is 0, it means the number is divisible by 3.
#       print(i,end=" ") # If the number is divisible by 3, this line prints the number. The end=" " argument ensures that each number is printed on the same line, separated by a space, instead of on a new line.
#    else:
#       continue #If the number is not divisible by 3, the continue statement simply skips the rest of the current iteration and moves on to the next number in the loop.


        #3 6 9 12 15 18 21 24 27 30


#3 Python program to check a given number is part of the Fibonacci series from 1 to 40.

# fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
# num1 = 22
# if num1 in fib:
#     print("It is a part of the series :", num1)
# else:
#     print("It is not a part of the series :", num1)

    #It is not a part of the series : 22

#4Python program to check authentication with the given username and password.

#
# name = "vinod"
# password = "vinod"
#
# if name == password:
#     print("It is valid")
# else:
#     print("It is not valid")




#5Python program to validate user_id in the list of user_ids.

# id_list = [1,2,3,5,6,7,8]
# id_ = 10
#
# if id_ in id_list:
#     print("Valid ID")
# else:
#     print("Invalid ID")


#6  Python program to check whether any given number is a palindrome.
# num1 = 121
# num2 = str(num1)
#
# if num1 == int(num2[::-1]):
#     print("It is a palindrome number")
# else:
#     print("It is not a palindrome number")

    #It is not a palindrome number
    #It is a palindrome number

#7 Python program to check if any given string is palindrome or not.

# str1 = 'viraj'
# str2 = str1[::-1]
#
# if str1 == str2:
#     print("It is a palindrome string")
# else:
#     print("It is not a palindrome string")


#8 Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.

# Input = 14
# Output = Fizz
# Input = 9
# Output = Buzz
# Input = 6
# Output = FizzBuzz

#
# num = 12
#
# if num%2 == 0 and num%3 == 0:
#     print("FizzBuzz")
# elif num%2 == 0:
#     print("Fizz")
# elif num%3 == 0:
#     print("Buzz")

#9Python program to check whether an alphabet is a consonant.
# char = "A"
# vowel = ["A","E","I","O","U","a","e","i","o","u"]
#
# if char not in vowel:
#     print("True")
# else:
#     print("False")
#


