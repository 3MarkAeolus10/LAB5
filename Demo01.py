import random
def Grade34():
    num1 = random.randint(0, 150)
    num2 = random.randint(0, 150)

    if num2 == 0:
        flag = random.randint(0, 2)
    else:
        flag = random.randint(0, 3)

    if flag ==0:
        print(num1," + ",num2," = ")
        sol = num1 + num2
    if flag ==1:
        print(num1," - ",num2," = ")
        sol = num1 - num2
    if flag ==2:
        print(num1," × ",num2," = ")
        sol = num1 * num2
    if flag ==3:
        print(num1," ÷ ",num2," = ")
        sol = num1 / num2
        if num1%num2==0:
            sol = round(sol, 2)

    return sol