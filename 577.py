import random

listOfSums = []
countOfSums = []
for i in range(1000):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    listOfSums.append(roll1 + roll2)
for roll in range(2, 13):
    countOfSums.append([roll, listOfSums.count(roll)])
print("[Roll, Number]")
for item in countOfSums:
    print(item)