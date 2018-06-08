import webhandler
import token

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


class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, query):
        """Answer a query"""
        tokens = token.tokenize(query)
        if tokens[0][1] == 'Is' and tokens[-1][1] == '?':
            return property(tokens[2:-1])
        return 85
