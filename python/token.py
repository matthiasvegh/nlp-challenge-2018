import re
import roman

def tokenize(s):
    tokens = []
    regexes = [
        ('whitespace', re.compile('^ +'), 0),
        ('number', re.compile('^[0-9]+'), 0),
        ('operator', re.compile('^[-+/*=]'), 0),
        ('parentheses', re.compile('^[()]'), 0),
        ('roman_number', re.compile('^([IVXLCDM]+) '), 1),
        ('roman_number', re.compile('^([IVXLCDM]+)$'), 1),
        ('word', re.compile('^[a-zA-Z]+'), 0),
        ('questionmark', re.compile('^\?'), 0)
    ]
    while len(s):
        for r in regexes:
            m = r[1].match(s)
            if m:
                val = m.group(r[2])
                if r[0] == 'number':
                    val = int(val)
                elif r[0] == 'roman_number':
                    val = roman.from_roman(val)

                tokens.append((r[0], val))
                s = s[len(m.group(r[2])):]
                continue

    return tokens

def filter_whitespace(tokens):
    return list(filter(lambda x: x[0] != 'whitespace', tokens))

def print_tokens(tokens):
    for t in tokens:
        print(t)

if __name__ == '__main__':
    print_tokens(tokenize('34 - (Is IV - asdasd?)'))
