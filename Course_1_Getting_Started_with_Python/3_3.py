score = input("Enter Score: ")
grade = float(score)


if grade >= 0.9 :
    fgrade = "A"
if grade >= 0.8 and grade < 0.9 :
    fgrade = "B"
if grade >= 0.7 and grade < 0.8:
    fgrade = "C"
if grade >= 0.6 and grade < 0.7 :
    fgrade = "D"
if grade < 0.6 :
    fgrade = "F"

elif grade < 0.0 or grade > 1.0 :
    print("please enter a score between 0.0 and 1.0")
    quit()

print(fgrade)
