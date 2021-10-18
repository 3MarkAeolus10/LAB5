import random

def Grade56():
    cishu = random.randint(1,4)
    number1 = random.uniform(0,1000)
    number2 = random.uniform(0,1000)
    number1 = round(number1,2)
    number2 = round(number2,2)

    if (cishu == 1):
        print(number1 , "+" , number2 ,"=")
        result = number1 + number2

    elif(cishu == 2):
        while (number1 < number2):
            number1 = random.uniform(0, 1000)
            number2 = random.uniform(0, 1000)
            number1 = round(number1, 2)
            number2 = round(number2, 2)

        print(number1, "-", number2,"=")
        result = number1 + number2

    elif (cishu == 3):
        print(number1, "×", number2, "=")
        result = number1 + number2

    elif (cishu == 4):
        while (number2 == 0):
            number2 = random.uniform(0, 1000)
            number2 = round(number2, 2)

        print(number1, "÷", number2, "=")
        result = number1 + number2

    return result