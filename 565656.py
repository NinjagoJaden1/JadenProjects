def sum_of_proper_divs(n):
    result = 0
    # for xs in [1, 2, 4]:
    #     result += xsl
    for possibilities in range(n):
        if n%(possibilities+1)==0:
            result += possibilities+1

    if result-n==n:
        return True
    else:
        return False

n=int(input("Enter any positive number: "))
print( sum_of_proper_divs(n))