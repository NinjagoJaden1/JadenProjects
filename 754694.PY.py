import random
def guess_number():
    realNumber=random.randrange(1,100)
    guess=0
    while guess != realNumber:
        guess=int(input("enter any positive integer from 1 to 100:"))
        if guess == realNumber:
            print("YOU GOT IT GREAT JOB ",realNumber,"is the number")
        elif guess > realNumber:
            print("YOUR NUMBER IS TOO HIGH")
        else:
            print("YOUR NUMBER IS TOO LOW")

    return realNumber
print(guess_number())