name = input("Hello I am Maverick, please tell me your name,\n")
print("Hello," + name + "!")
choice = input("Would you like to do (M)aths or (E)xit? \n")
if choice.lower() == "m":
    print("Maths it is then!")
    choice = input("would you like to do (A)ddition, (S)ubtraction, (M)ultiplication, or (D)ivision? \n")
    if choice.lower() == "a":
        num1 = float(input("what is the first addend? \n"))
        num2 = float(input("what is the second addend? \n"))
        ans = num1 + num2
        print("that is equal to " + str(ans) + "!")
    elif choice.lower() == "s":
        num1 = float(input("what is the minuend? \n"))
        num2 = float(input("what is the subtrahend? \n"))
        ans = num1 - num2
        print("that is equal to " + str(ans) + "!")
    elif choice.lower() == "m":
        num1 = float(input("what is the multiplicand? \n"))
        num2 = float(input("what is the multiplier? \n"))
        ans = num1 * num2
        print("that is equal to " + str(ans) + "!")
    elif choice.lower() == "d":
        num1 = float(input("what is the dividend? \n"))
        num2 = float(input("what is the divisor? \n"))
        ans = num1 / num2
        print("that is equal to " + str(ans) + "!")
    else:
        print("that is not a valid option!")
elif choice.lower() == "e":
    print("good bye!")
    exit()
else:
    print("that is not a valid choice")

