print("-----WELCOME TO NUMBER GUESSING GAME-----")
print("--PLEASE NOTE THAT YOU HAVE ONLY 9 CHANCES TO WIN THE GAME!!")
n=18
guesses=1
while(guesses<=9):
    print("--ENTER YOUR NUMBER: ",end="")
    n1=int(input())
    if n1>18:
        print("--KINDLY ENTER A LESSER NUMBER FROM",n1)
    elif n1<18:
        print("--ENTER A GREATER NUMBER FROM",n1)
    else:
        print("--CONGRATULATIONS!!YOUR GUESSES NUMBER IS CORRECT.")
        print("--YOU ARE TOOK TO CHANCES TO FINISH ",guesses)
        break
    print("--",9-guesses,"CHANCES LEFT.")
    guesses=guesses+1
if (guesses>9):
    ("#GAME OVER.")
print("--THANK YOU FOR A PARTICIPATE.")
