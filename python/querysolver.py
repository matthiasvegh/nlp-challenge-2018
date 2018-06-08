import webhandler
import token
import infix_parser

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return 'No'
        return 'Yes'
    return 'No'

def property(tokens):
    value = int(tokens[0][1])
    print('getting property of ' + str(value))
    remainder = str.join('', [token[1] for token in tokens[2:]])
    properties = {
        'a leap year': isLeapYear
    }
    return properties[remainder](value)


def convert(tokens):
    print('converting')
    value = int(tokens[0][1])
    unitFrom = tokens[2][1]
    unitTo = tokens[6][1]
    conversions = {
        ('days', 'hours'): 24,
        ('days', 'minutes'): 24*60,
        ('days', 'seconds'): 24*3600,
        ('hours', 'minutes'): 60,
        ('minutes', 'seconds'): 60,
        ('hours', 'seconds'): 3600,
        ('metres', 'feet'): 3.28084,
        ('metres', 'yards'): 1.09361,
        ('metres', 'inches'): 39.3701,
        ('yards', 'feet'): 3,
        ('yards', 'inches'): 36,
        ('feet', 'inches'): 12,
        ('miles', 'kilometres'): 1.60934,
        ('miles', 'yards'): 1760,
    }
    try:
        coeff = conversions[(unitFrom, unitTo)]
        return str(value * coeff) + ' ' + unitTo
    except KeyError:
        try:
            coeff = conversions[(unitTo, unitFrom)]
            return str(value / coeff) + ' ' + unitTo
        except KeyError:
            return 85

def solveSimple(tokens):
    print('Solving simple equation')
    coeff = int(tokens[0][1])
    constant = int(tokens[8][1])
    result = int(tokens[-1][1])
    solution = (result - constant) / coeff
    if solution == int(solution):
        return int(solution)


def solveMult(tokens):
    print('Solving mult equation')
    coeff = int(tokens[0][1])
    coeff2 = int(tokens[8][1])
    result = int(tokens[-1][1])
    solution = (result / coeff2) / coeff
    if solution == int(solution):
        return int(solution)


class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, query):
        """Answer a query"""
        tokens = token.tokenize(query)
        if tokens[0][1] == 'Is' and tokens[-1][1] == '?':
            return property(tokens[2:-1])
        if len(tokens) == 7 and tokens[-3][1] == 'in':
            return convert(tokens)
        if len(tokens) == 13 and tokens[-3][1] == '=' and tokens[6][1] == '+':
            return "x = " + str(solveSimple(tokens))
        if len(tokens) == 13 and tokens[-3][1] == '=' and tokens[6][1] == '*':
            return "x = " + str(solveMult(tokens))
        try:
            result = infix_parser.infix_eval(query)
            if int(result) == result:
                return int(result)
            return result
        except:
            return 85
