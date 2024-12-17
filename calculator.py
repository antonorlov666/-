try:

    a = int(input('введите число a: '))  # число номер 0
    b = int(input('введите число b: '))  # число номер 1
    mat_symbol = input('введите математический символ: ')  # че делать с числом


    def summ(a, b):  # сумма чисел a и b
        sm = a + b
        return print(sm)


    def sub(a, b):  # разность чисел a и b
        s = a - b
        return print(s)


    def div(a, b):  # частность чисел a и b
        d = a / b
        return print(d)


    def multi(a, b):  # произведение чисел a и b
        m = a * b
        return print(m)


    def deg(a, b):  # функция для возведения одного числа в степень другого
        c = a ** b
        return print(c)


    if mat_symbol == '+':
        summ(a, b)
    elif mat_symbol == '-':
        sub(a, b)
    elif mat_symbol == '/':
        div(a, b)
    elif mat_symbol == '*':
        multi(a, b)
    elif mat_symbol == '^':
        deg(a, b)


except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print('Это что ещё такое?')