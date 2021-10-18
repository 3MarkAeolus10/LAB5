while True:
    grade = input('please enter your grade: ');
    g = int(grade);
    if g >= 1 and g <= 6:
        print("your grade is", g);
        break;
    else:
        print('Error! Please enter again.');

qnum = input("Please enter the number of question: ");
n = int(qnum);
print("The test contains", n, "questions.");

# 判断对错
right = 0;
score = 0;
answer = input('Please enter your answer: ');
if answer == resulst:
    right = right + 1;
# 算分
score = 100 * (right / n);
if score == 100:
    print("End ! All right, that is great! Your score is 100.");
else:
    print("End ! Wrong question. Your score is", score, ".");