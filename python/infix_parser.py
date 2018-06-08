from token import *

def precendence(op):
    if op == '-' or op == '+':
        return 1
    if op == '*' or op == '/':
        return 2


def infix_eval(s):
    tokens = filter_whitespace(tokenize(s))

    output_tokens = []
    operator_stack = []

    for token in tokens:
        if token[0] == 'number':
            output_tokens.append(token)
        elif token[0] == 'operator':
            while len(operator_stack):
                top = operator_stack[-1]
                if top[0] != 'operator' or precendence(token[1]) > precendence(top[1]):
                    break
                if top[1] == '(':
                    break
                output_tokens.append(top)
                operator_stack.pop()
            operator_stack.append(token)
        elif token[1] == '(':
            operator_stack.append(token)
        elif token[1] == ')':
            while len(operator_stack):
                top = operator_stack[-1]
                if top[1] == '(':
                    operator_stack.pop()
                    break
                output_tokens.append(top)
                operator_stack.pop()

    while len(operator_stack):
        output_tokens.append(operator_stack[-1])
        operator_stack.pop()

if __name__ == '__main__':
    print(infix_eval('(34 + 35) * 3'))
