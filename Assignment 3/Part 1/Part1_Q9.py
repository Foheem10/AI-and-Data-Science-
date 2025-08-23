# Q9: Check Pass or Fail based on score

def check_score(score):
    if score > 60:
        return "Pass"
    else:
        return "Fail"

s = int(input("Enter your score: "))
print(check_score(s))
