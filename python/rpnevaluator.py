import webhandler

class Op(object):
    pass

class Plus(Op):
    def __call__(self, l, r):
        return l + r

class Minus(Op):
    def __call__(self, l, r):
        return l - r

class Multiply(Op):
    def __call__(self, l, r):
        return l * r

class Divide(Op):
    def __call__(self, l, r):
        return l // r

class RpnEvaluator(object):
    def __init__(self):
        pass

    def _tokenize(self, string):
        return string.split(' ')

    def _parseOp(self, op):
        ops = {
            '+': Plus(),
            '-': Minus(),
            '*': Multiply(),
            '/': Divide()
        }
        return ops[op]

    def _parseToken(self, token):
        try:
            return self._parseOp(token)
        except KeyError as ex:
            return int(token)

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""
        tokens = self._tokenize(rpn)
        print(tokens)
        stack = []
        values = [self._parseToken(token) for token in tokens]
        for value in values:
            if isinstance(value, Op):
                arg2 = stack.pop()
                arg1 = stack.pop()
                tmp = stack.append(value(arg1, arg2))
            else:
                stack.append(value)
        return stack[0]

