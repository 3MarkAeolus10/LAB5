import random

def Grade12():
    def cal(flag, num1, num2):
        if flag == 0:
            return (num1 + num2)
        else:
            return (num1 - num2)

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    flag = random.randint(0, 1)
    if flag == 0:
        print(num1, " + ", num2, " = ?")
    else:
        print(num1, " - ", num2, " = ?")
    sol = cal(flag, num1, num2)
    return sol
def Grade34():
    num1 = random.randint(0, 150)
    num2 = random.randint(0, 150)

    if num2 == 0:
        flag = random.randint(0, 2)
    else:
        flag = random.randint(0, 3)

    if flag == 0:
        print(num1, " + ", num2, " = ?")
        sol = num1 + num2
    if flag == 1:
        print(num1, " - ", num2, " = ?")
        sol = num1 - num2
    if flag == 2:
        print(num1, " × ", num2, " = ?")
        sol = num1 * num2
    if flag == 3:
        print(num1, " ÷ ", num2, " = ?")
        sol = num1 / num2
        if num1 % num2 == 0:
            sol = round(sol, 2)
    return sol
def Grade56():
    flag = random.randint(1, 4)
    num1 = random.uniform(0, 1000)
    num2 = random.uniform(0, 1000)
    num1 = round(num1, 2)
    num2 = round(num2, 2)
    if (flag == 1):
        print(num1, " + ", num2, " = ?")
        sol = num1 + num2
    elif (flag == 2):
        while (num1 < num2):
            num1 = random.uniform(0, 1000)
            num2 = random.uniform(0, 1000)
            num1 = round(num1, 2)
            num2 = round(num2, 2)
        print(num1, " - ", num2, " = ?")
        sol = round(num1 - num2,2)
    elif (flag == 3):
        print(num1, " × ", num2, " = ?")
        sol = num1 * num2
    elif (flag == 4):
        while (flag == 0):
            num2 = random.uniform(0, 1000)
            num2 = round(num2, 2)
        print(num1, " ÷ ", num2, " = ?")
        sol = round(num1 / num2 ,2)
    return sol
def judge(right,sol):
    answer = input('Please enter your answer: ')
    if float(answer) == sol:
        right = right + 1
    return right
def score(right):
    score = 100 * (right / n)
    if score == 100:
        print("End ! All right, that is great! Your score is 100.")
    else:
        print("End ! Wrong question. Your score is", score, ".")


right = 0
grade = input("please enter your grade: ")
gradeInt = int(grade)
while True:
    if gradeInt >= 1 and gradeInt <= 6:
        print("your grade is", gradeInt)
        break
    else:
        print('Error! Please enter again.')
questionNum = input("Please enter the number of question: ")
n = int(questionNum)
print("The test contains", n, "questions.")
if gradeInt==1 or gradeInt==2:
    for i in range(n):
        sol = Grade12()
        right = judge(right,sol)
    score(right)
if gradeInt==3 or gradeInt==4:
    for i in range(n):
        sol = Grade34()
        right = judge(right,sol)
    score(right)
if gradeInt==5 or gradeInt==6:
    for i in range(n):
        sol = Grade56()
        right = judge(right,sol)
    score(right)




