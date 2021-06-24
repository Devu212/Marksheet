print("# Welcome To CBSE Calculator # \n")
print("--ENTER YOUR TOTAL MARKS HERE:- ", end="")
while(True):
    n1=int(input())
    if n1==600:
        print("YOU CAN GO AHEAD.")
        break
    else:
        print("SORRY! YOU ENTERED FALSE.ENTER AGAIN!")
        continue
print("1.ENTER YOUR SCIENCE MARKS HERE: ")
while(True):
    n2 = float(input())
    if 100>=n2>=0:
        break
    else:
        print("SORRY! YOU ENTERED FALSE.ENTER AGAIN!")
        continue
print("2.ENTER YOUR MATHEMATICS MARKS HERE: ")
while(True):
    n3 = float(input())
    if 100>=n3>=0:
        break
    else:
        print("SORRY! YOU ENTERED FALSE.ENTER AGAIN!")
        continue
print("3.ENTER YOUR SOCIAL SCIENCE MARKS HERE: ")
while(True):
    n4 = float(input())
    if 100>=n4>=0:
        break
    else:
        print("SORRY! YOU ENTERED FALSE.ENTER AGAIN!")
        continue
print("4.ENTER YOUR ENGLISH MARKS HERE: ")
while(True):
    n5 = float(input())
    if 100>=n5>=0:
        break
    else:
        print("SORRY! YOU ENTERED FALSE.ENTER AGAIN!")
        continue
print("5.ENTER YOUR COMPUTER APPLICATIONS MARKS HERE: ")
while(True):
    n6 = float(input())
    if 100>=n6>=0:
        break
    else:
        print("SORRY! YOU ENTERED FALSE.ENTER AGAIN!")
        continue
print("6.ENTER YOUR SANSKRIT MARKS HERE: ")
while(True):
    n7 = float(input())
    if 100>=n7>=0:
        break
    else:
        print("SORRY! YOU ENTERED FALSE.ENTER AGAIN!")
        continue
var1=(n2+n3+n4+n5+n6+n7)
print("--YOU TOTAL OBTAINED MARKS",var1,"OUT OF", n1)
var2=var1*100/n1
print("--YOUR PERCENTAGE IS::", var2)
if 99.999>=var2>=90:
    print("--CONGRATULATIONS!!")
    print("--YOU ARE EXELLENT. YOU ARE THE TOPPER. GRADE:A+")
elif 89.99>=var2>=85:
    print("--CONGRATULATIONS!!")
    print("--YOU ARE GREAT. GRADE:A")
elif 84.99>=var2>=80:
    print("--CONGRATIONS!!")
    print("--YOU ARE SUPERB. GRADE:B+")
elif 79.99>=var2>=75:
    print("--CONGRATULATIONS!!")
    print("--YOU ACHIEVED VERY GOOD SCORE. GRADE:B")
elif 74.99>=var2>=70:
    print("--CONGRATULATIONS!!")
    print("--YOU ACHIEVED GOOD SCORE. GRADE=C+")
elif 69.99>=var2>=65:
    print("--CONGRATULATIONS!!")
    print("--YOU ACHIEVED AVERAGE SCORE. GRADE=C")
elif 64.99>=var2>=60:
    print("--CONGRATULATIONS!!")
    print("--YOU ACHIEVED ACCEPTABLE SCORE. GRADE=D+")
elif 59.99>=var2>=55:
    print("--CONGRATULATIONS!!")
    print("--YOU ACHIEVED NORMAL SCORE, GRADE=D")
elif 54.99>=var2>=35:
    print("--CONGRATULATIONS!!")
    print("--YOU ACHIEVED JUST PASS CLASS.")
else:
    print("--YOU ARE FAIL!! BETTER LUCK NEXT TIME.")