import random 

def generate_math_question(a, b):
    d = ""
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice("+-*/")
    d = f'{num1} {operator} {num2}'
    return d


def check_answer(a, b):
    try:
        b = float(b)
        if eval(a) == b:
            return True
        else:
            return False
        # return eval(a) == b
    except ValueError:
        return False


def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        quistion = generate_math_question(1, 5)
        user_unsword = input(f"{quistion}=")
        if check_answer(quistion, user_unsword):
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers / 7 > 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers / 7 > 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(7)