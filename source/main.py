from parser import *

def main():
    
    while True:
        expression = input()
        print(is_expr(filter_expression(expression)), "\n")

if __name__ == '__main__':
    import sys

    main()