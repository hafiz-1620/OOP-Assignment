grades = [85, 78, 92, 45, 33, 67, 88, 41] 
#catagories the grades
for i in grades:
    if i>80:
        print("Score:",i, "- Grade: A")
    elif 60<=i<=80:
        print("Score:",i, "- Grade: B")
    elif 40<=i<=60:
        print("Score:",i, "- Grade: C")
    elif i<40:
        print("Score:",i, "- Grade: F")

#Update the grades
boosted_grades = [grade * 1.05 for grade in grades]
print("\nBoosted grades:",boosted_grades)
#grades above 90
high_grades = [grade for grade in boosted_grades if grade > 90]
print("\nGrades above 90:",high_grades)


       

    
