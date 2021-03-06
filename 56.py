hours=int(input("Enter any positive integer for hours "))
minutes=int(input("Enter any positive integer for minutes "))
seconds=int(input("Enter any positive integer for seconds "))
def convert_to_seconds(hours, minutes, seconds) :
    seconds1=60 * minutes
    seconds2=3600 * hours
    total= seconds+seconds2+seconds1
    return total

print(convert_to_seconds(hours,minutes,seconds))