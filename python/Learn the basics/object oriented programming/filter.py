# filter(condition, collection) = return all elements that pass a condition



grades = [91, 32, 83, 44, 75, 56, 67]



passing_grades = list(filter(lambda grade: grade >= 60, grades))



print(passing_grades)