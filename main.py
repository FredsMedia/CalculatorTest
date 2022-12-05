def end():
    repeat = input('Would you like to do another calculation? (Y or N, caps sensitive)')

    if repeat == 'Y':
        calculate()

    if repeat == "N":
        exit()


def add():
    num1 = float(input('what is your first number? '))
    num2 = float(input('what is your second number? '))

    answer = num1 + num2

    print(answer)
    end()


def sub():
    num1 = float(input('what is your first number? '))
    num2 = float(input('what is your second number? '))

    answer = num1 - num2

    print(answer)
    end()


def div():
    num1 = float(input('what is your first number? '))
    num2 = float(input('what is your second number? '))

    try:
        answer = num1 / num2
    except ZeroDivisionError:
        answer = 0

        print(answer)
        end()

    print(answer)
    end()


def mul():
    num1 = float(input('what is your first number? '))
    num2 = float(input('what is your second number? '))

    answer = num1 * num2

    print(answer)
    end()


repeat = "Y"


def calculate():
    sign = input('Would you like to add, subtract, divide, or multiply? ')

    if sign == "add":
        add()

    elif sign == "subtract":
        sub()

    elif sign == "divide":
        div()

    elif sign == "multiply":
        mul()


calculate()
