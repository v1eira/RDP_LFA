def is_expr(expr): # Verifica se a string de entrada é uma expressão válida
    right = "" ; op = ""
    msg = "Error: invalid expression."
    plusMinus = ["+", "-"] ; operands = ["*", "/", "//", "%", "^", "e"]
    left = 0.0
    firstElement = 0 ; seeNumber = 0 ; countParenthesis = 0

    verify_parenthesis(expr)

    for i in range(0, len(expr)):
        if expr[i] == "(":
            countParenthesis += 1
        if expr[i] == ")":
            countParenthesis -= 1
        if expr[i] not in plusMinus and seeNumber == 0:
            if expr[i] in operands: # Se a expressão começa com +- E operands ou operands
                raise Exception(msg)
            seeNumber = 1
            right += expr[i]
        elif expr[i] in plusMinus and seeNumber == 1 and expr[i-1] not in operands and expr[i-1] not in plusMinus:
            if countParenthesis == 0:
                if firstElement == 0:
                    firstElement = 1
                    left = is_term(right)
                    op = expr[i]
                    right = ""
                else:
                    left = calc(left, is_term(right), op)
                    op = expr[i]
                    right = ""
            else:
                right += expr[i]
        else:
            right += expr[i]

    if right != "":
        if left != 0.0:
            left = calc(left, is_term(right), op)
        else:
            left = is_term(right)
    
    return left


def is_term(term): # Verifica se a string de entrada é um termo válido
    right = "" ; op = ""
    msg = "Error: invalid term."
    operands = ["*", "/", "//", "%"]
    left = 0.0
    firstElement = 0 ; countParenthesis = 0

    for i in range(0, len(term)):
        # Caso right tenha recebido "/" na posição anterior. "//" já está salvo em op
        if right == "" and term[i] == "/": #len(right) > 0 and right[0] == "/":
            continue
        if term[i] == "(":
            countParenthesis += 1
        if term[i] == ")":
            countParenthesis -= 1
        if term[i] in operands:
            # Caso venha um operando e não tenha nada após ele
            if (i == len(term)-1) or (term[i+1] == "/" and i+1 >= len(term)):
                raise Exception(msg)
            if countParenthesis == 0:
                if firstElement == 0:
                    firstElement = 1
                    left = is_factor(right)
                    if term[i] == "/" and term[i+1] == "/":
                        op = term[i] + term[i+1]
                    else:
                        op = term[i]
                    right = ""
                else:
                    left = calc(left, is_factor(right), op)
                    op = term[i]
                    right = ""
            else:
                right += term[i]
        else:
            right += term[i]
    
    if right != "":
        if left != 0.0:
            left = calc(left, is_factor(right), op)
        else:
            left = is_factor(right)
    
    return left


def is_factor(factor): # Verifica se a string de entrada é um fator válido
    base = ""
    msg = "Error: invalid factor."
    
    for i in range(0, len(factor)):
        if factor[i] == "^":
            break
        base += factor[i]
    
    base = is_base(base)

    if i < len(factor) and factor[i] == "^":
        i += 1
        if i >= len(factor):
            raise Exception(msg)
        
        rest = ""
        
        for j in range(i, len(factor)):
            rest += factor[j]
        
        return base ** is_factor(rest)
    
    return base


def is_base(base): # Verifica se a string de entrada é uma base válida
    num = "" ; rest = "" ; expr = ""
    msg = "Error: invalid base."
    operands = ["+", "-"]

    if base[0] == "+":
        return is_base(base = base.replace("+", "", 1))
    
    if base[0] == "-":
        return -1 * is_base(base = base.replace("-", "", 1))
    
    if base[0] == "(":
        if base[len(base)-1] == ")":    
            for i in range(1, len(base)-1):
                expr += base[i]
            
            return is_expr(expr)
        else:
            raise Exception(msg)
    
    return is_number(base)


def is_number(number): # Verifica se a string de entrada é um número válido
    msg = "Error: invalid number."
    operands = ["+", "-"]
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


def is_digit(digit):  # Verifica se o caracter de entrada é um dígito válido
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    return True if digit in digits else False


def calc(num1, num2, op): # Retorna o resultado das operações (+, -, *, /, // e %) entre dois números
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
    elif op == "%":
        return num1 % num2
    else:
        raise Exception("Error: invalid operand.")


def verify_parenthesis(expression): # Verifica se todos os parênteses que foram abertos na expressão foram fechados
    count = 0

    for i in range(0, len(expression)):
        if expression[i] == "(":
            count += 1
        if expression[i] == ")":
            count -= 1
    
    if count != 0:
        raise Exception("Error: invalid number of parenthesis.")


def filter_expression(expression):  # Remove espaços em branco e torna a string de entrada minúscula
    expression = "".join(expression.split()).lower()

    return expression