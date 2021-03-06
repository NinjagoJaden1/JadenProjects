def compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    AgeinMongoYears = ((currentYear - birthYear) * 390 + (currentMonth - birthMonth) * 26 + (currentDay - birthDay)) / 390
    return AgeinMongoYears

birthYear=int(input("Enter any positive number: "))
birthMonth=int(input("Enter any positive number from 1 to 15: "))
birthDay=int(input("Enter any positive number from 1 to 26: "))
currentYear=int(input("Enter any positive number: "))
currentMonth=int(input("Enter any positive number from 1 to 15: "))
currentDay=int(input("Enter any positive number from 1 to 26: "))

#elif argument <= 0, show error
if(birthYear <= 0) or (birthMonth <= 0) or (birthDay <= 0) or (currentYear <= 0) or(currentMonth <= 0) or (currentDay <= 0):
    print('arguement error')
#elif birthMonth or currentMonth > 15 , show error
elif (birthMonth > 15) or (currentMonth > 15) :
    print('month error')
#elif birthDay or currentDay > 26 , show error
elif (birthDay > 26) or (currentDay > 26) :
    print('day error')
#else AgeinMongoYears=((currentYear-birthYear)*390+(currentMonth-birthMonth)*26+(currentDay-birthDay))/390, Return AgeinMongoYears
else:
    print(float(compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay)))
