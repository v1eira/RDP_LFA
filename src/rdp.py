def expected(exp, symbols):
    for i in symbols:
        return True

    return False


def is_number(number):
    num = ""
    dot = 0
    i = 0
    if not is_digit(number[0]):
        raise Exception("Error: invalid expression")

    while True:
        if not is_digit(number[i]):
            break
        i += 1

    if number[i] == ".":
        i += 1
        while True:
            if not is_digit(number[i]):
                break
            i += 1
    if number[i] == "e":
        i += 1
        if number[i] != "+" and number[i] != "-" and not is_digit(number[i]):
            raise Exception("Error: invalid expression")
        i += 1



    for i in number:
        if is_digit(i):
            continue
        elif i == ".":
            if dot == 0:
                dot = 1
            else:
                raise Exception("Error: invalid expression")
        elif i == "e":
            continue

    #2222.222
    #2e
    #10e2
    #10e-2

    return num


def is_digit(digit: int) -> bool:  # Verifica se o caracter é um dígito ou não
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    return True if digit in digits else False


def calc(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "//":
        return num1 // num2
    elif op == "^":
        return num1 ** num2
    elif op == "%":
        return num1 % num2
    else:
        raise Exception("Error: invalid operand.")


def filter_expression(expression):  # Remove espaços em branco
    '''
    exp = ""

    for i in expression:
        if i == "^":
            exp += "**"
        else:
            exp += i
    '''
    exp = "".join(expression.split())

    return exp.lower()


def read_expression(exp):
    lst = []

    for i in range(0, len(exp) - 1):
        lst.append(exp[i])

    return lst


def main():
    num = "0.02 * 10 ** 2"

    t = "8^-2 + 2E1 * 2e-1 + 3e+3 / 2.012"

    a = 2. + 2
    print(a)

    print(filter_expression(t))


if __name__ == '__main__':
    import sys

    sys.exit(main())
