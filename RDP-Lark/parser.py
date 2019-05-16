from lark import Lark, Transformer

grammar = """
    expr: term (("+" | "-") term)*
    term: factor (("*" | "/" | "//" | "%") factor)*
    factor: base ("^" factor)?
    base: ("+" | "-") base
        | number
        | "(" expr ")"
    number: digit+ "."? digit* (("E" | "e") ("+" | "-")? digit+)?
    digit: "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
"""

parser = Lark(grammar, start="expr")

def parser_result(expression):    
    expression = "".join(expression.split())
    try:
        parser.parse(expression)
        return True
    except:
        return False