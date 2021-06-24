print("Enter Your First Number: ")
num1=(int(input()))
print("Enter Your Second Number: ")
num2=(int(input()))
print("Choose Your Operator(-,+,/,%): ")
num3=(input())
if num1==56 and num2==9 and num3=="+":
    print("Your Answer Is 77.")
elif num1==45 and num2==3 and num3=="*":
    print("Your Answer Is 555.")
elif num1==56 and num2==6 and num3=="/":
    print("Your Answer Is 4.")
elif num3=="*":
    print("Your Answer Is ", num1*num2)
elif num3=="/":
    print("Your Answer Is ", num1/num2)
elif num3=="+":
    print("Your Answer Is ", num1+num2)
elif num3=="-":
    print("Your Answer Is ", num1-num2)
else:
    print("Thank You!!See You Next Time.")