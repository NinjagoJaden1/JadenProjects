fourdigitnumber = int(input("Enter the four digit number: "))
fourthdigit=fourdigitnumber%10
thirddigit=(fourdigitnumber%100)//10
seconddigit=(fourdigitnumber%1000)//100
firstdigit=fourdigitnumber//1000
fourdigitnumber=fourthdigit*1000+thirddigit*100+seconddigit*10+firstdigit
print(fourdigitnumber)