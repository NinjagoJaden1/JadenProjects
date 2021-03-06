currentHour = int(input("Enter the current hour: "))
hoursToAdd = int(input("Enter the number of hours to add: "))
totaltime=((currentHour+hoursToAdd)%12)
if totaltime == 0 :
   totaltime=totaltime+12
print(totaltime)