import random

n = random.randint(1,100) 
g = int(input("Enter number :"))

count = 0
flag = 0
while flag!=1 :
    count+=1 
    if g < n :
        print("Guess Higher")
        g = int(input("Enter number :"))

    elif g>n :
        print("Guess Lower")
        g = int(input("Enter number :"))
    else :
        flag = 1
        print("Correct guess")
        print("Number of guesses :", count)
    
