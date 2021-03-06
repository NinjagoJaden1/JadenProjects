n = int(input("Enter a positive integer n: "))
if n==1 :
    print(1)
elif n==2 :
    print(1)
else:
    m=3
    oneBefore=1
    twoBefore=1
    current=0
    print('A', m, oneBefore, twoBefore, current)
    while m!=n:
        current=oneBefore+twoBefore
        print('B', m, oneBefore, twoBefore, current)
        if m==n :
            print(current)
        else :
            m=m+1
            print('C', m, oneBefore, twoBefore, current)
            twoBefore=oneBefore
            print('D', m, oneBefore, twoBefore, current)
            oneBefore=current
            print('E', m, oneBefore, twoBefore, current)
    current=oneBefore+twoBefore
    print('F', m, oneBefore, twoBefore, current)
    print(current)