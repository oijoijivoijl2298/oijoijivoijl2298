import random
nummer = random.randint(1,100)
win = False
beurten =0
while win==False:
    Your_guess = int(input("Enter a number between 1 and 100"))
    beurten +=1
    if nummer==Your_guess:
        print("good boy you done right today!")
        print("score: aantal beurten gehad: ",beurten)
        win == True
        break
    else:
     if nummer>Your_guess:
        print("Your Guess was low, Please enter a higher number")
     else:
        print("your guess was high, please enter a lower number")
        #comment for change sync to vs code
