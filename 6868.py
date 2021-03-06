def assign_letter_grade(score):
    score = round(score)
    if  100 >= score >= 96:
        grade = "A+"
        return grade
    elif   95 >= score >= 88:
        grade="A"
        return grade
    elif  87 >= score >= 85:
        grade="B+"
        return grade
    elif  84 >= score >= 80:
        grade="B"
        return grade
    elif  79 >= score >=77:
        grade="C+"
        return grade
    elif 76 >= score >= 70:
        grade="C"
        return grade
    elif 69 >= score >= 66:
        grade="D"
        return grade
    elif 65 >= score >= 50:
        grade="F"
        return grade
    else:
        grade= "I"
        return grade
score=int(input("Enter any positive number from 0 to 100: "))
print(assign_letter_grade(score))