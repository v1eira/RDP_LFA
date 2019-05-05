def expected(exp, symbols):
    for i in symbols:
        return True

    return False


def is_term(term):
    left = 0.0
    right = ""
    operands = ["*", "/", "//", "%"]
    aux = 0

    for i in range(0, len(term)):
        if term[i] in operands:
            if aux == 0:
                aux = 1
                left = is_factor(right)
                op = term[i]
                right = ""
            elif aux == 1:
                left = calc(left, is_factor(right), op)
                op = term[i]
                right = ""
        else:
            right += term[i]
    
    if right != "":
        if left != 0.0:
            left = calc(left, is_factor(right), op)
        else:
            left = is_factor(right)
    
    return left


def is_factor(factor):
    msg = "Error: invalid factor"
    base = ""
    
    for i in range(0, len(factor)):
        if factor[i] == "^":
            break
        base += factor[i]
    
    base = is_base(base)

    if factor[i] == "^":
        i += 1
        
        if i >= len(factor):
            raise Exception(msg)
        
        rest = ""
        
        for j in range(i, len(factor)):
            rest += factor[j]
        
        return base ** is_factor(rest)
    
    return base


def is_base(base): # Verifica se a base de entrada é uma base válida
    msg = "Error: invalid base"
    operands = ["+", "-"]
    num = ""
    rest = ""
    
    if base[0] == "+":
        return is_base(base = base.replace("+", "", 1))
    
    if base[0] == "-":
        return -1 * is_base(base = base.replace("-", "", 1))
    
    '''for i in range(0, len(base)):
        if base[i] in operands:
            break
        num += base[i]
    
    for j in range(i, len(base)):
        rest += base[j]'''

    if is_number(base):
        return is_number(base)
    
    if base[0] == "(":
        exp = is_expr(base)
        
        if not exp:
            raise Exception(msg)
        
        if base[len(base)-1] == ")":
            return exp
    else:
        raise Exception(msg)


def is_number(number): # Verifica se a string de entrada é um número válido
    operands = ["+", "-"]
    msg = "Error: invalid number"
    i = 0
    
    if not is_digit(number[0]):
        raise Exception(msg)

    while i < len(number):
        if not is_digit(number[i]):
            break
        i += 1

    if i < len(number) and number[i] == ".":
        i += 1
        while i < len(number):
            if not is_digit(number[i]):
                break
            i += 1
    
    
    if i < len(number) and number[i] == "e":
        i += 1
        
        if i >= len(number): # Se não há nada após o "e"
            raise Exception(msg)
        
        if (number[i] not in operands and not is_digit(number[i])): # Se o que vem após o "e" não é dígito nem está em operands
            raise Exception(msg)
        
        i += 1
        
        if number[i-1] in operands and i >= len(number): # Se o último caracter está em operands
            raise Exception(msg)
        
        if i < len(number):
            while i < len(number):
                if not is_digit(number[i]):
                    raise Exception(msg)
                i += 1
    elif i < len(number) and number[i] != "e": # Se o último caracter não é dígito nem "e"
        raise Exception(msg)
    
    return float(number)


def is_digit(digit: int) -> bool:  # Verifica se o caracter de entrada é um dígito válido
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    return True if digit in digits else False


def calc(num1, num2, op):
    if op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "//":
        return num1 // num2
    elif op == "%":
        return num1 % num2
    else:
        raise Exception("Error: invalid operand.")


def filter_expression(expression):  # Remove espaços em branco e torna a string minúscula
    expression = "".join(expression.split()).lower()

    return expression


def read_expression(exp):
    lst = []

    for i in range(0, len(exp) - 1):
        lst.append(exp[i])

    return lst


def main():
    num = "0.02 * 10 ** 2"

    t = "8^-2 + 2E1 * 2e-1 + 3e+3 / 2.012"

    oi = "-----0.02e2"
    #print(is_base(oi))

    asd = "----2^2^-2^1"
    asd = "-2^2^1*2*-2*2*-22.5"
    print(asd)
    print(is_term(asd))

    a = "222e-2"
    #print(is_number(a))

    #print(filter_expression(t))


if __name__ == '__main__':
    import sys

    main()

 