from parser import *

def main():
    
    while True:
        expression = input()
        result = parser_result(expression)
        if result is True:
            print("Valid expression.\n")
        else:
            print("Invalid expression.\n")

if __name__ == '__main__':
    import sys

    main()