from token import *

def precendence(op):
    if op == '-' or op == '+':
        return 1
    if op == '*' or op == '/':
        return 2


def to_rpn_tokens(tokens):
    tokens = filter_whitespace(tokens)

    output_tokens = []
    operator_stack = []

    for token in tokens:
        if token[0] == 'number' or token[0] == 'roman_number':
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

    return output_tokens


def infix_eval(s):
    tokens = tokenize(s)
    roman_num = False
    for token in tokens:
        if token[0] == 'roman_number':
            roman_num = True

    rpn = to_rpn_tokens(tokens)
    stack = []
    for t in rpn:
        if t[0] == 'operator':
            if t[1] == '+':
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs + rhs)
            if t[1] == '-':
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs - rhs)
            if t[1] == '*':
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs * rhs)
            if t[1] == '/':
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs / rhs)
        else:
            stack.append(t[1])

    res = stack[-1]
    if int(res) == res:
        res = int(res)

    if roman_num:
        res = roman.to_roman(res)
    return res

if __name__ == '__main__':
    print(infix_eval('VI + IV'))
