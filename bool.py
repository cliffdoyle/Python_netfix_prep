"""boolean operators and,or and not"""

gender='female'
age=70

if gender=='female' and age>=70:
    print('senior female')
    
    
semester_average=83
final_exam=95
#Short circuit evaluation
if semester_average>=90 or final_exam>=90:
    print('Student gets an A')