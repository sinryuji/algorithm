total = 0
totalScore = 0

def getGrade(grade):
    if grade == "A+":
        return 4.5
    elif grade == "A0":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B0":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C0":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D0":
        return 1.0
    else:
        return 0.0

for _ in range(20):    
    subject, score, grade = input().split()
    if (grade == "P"):
        continue
    total += float(score) * getGrade(grade)
    totalScore += float(score)
print(total / totalScore)