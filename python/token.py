import re

def tokenize(s):
    tokens = []
    regexes = [
        ('whitespace', re.compile('^ +')),
        ('number', re.compile('^[0-9]+')),
        ('operator', re.compile('^[-+/*=]')),
        ('parentheses', re.compile('^[()]')),
        ('roman_number', re.compile('^[IVXLCDM]+ ')),
        ('word', re.compile('^[a-zA-Z]+')),
        ('questionmark', re.compile('^\?'))
    ]
    while len(s):
        for r in regexes:
            m = r[1].match(s)
            if m:
                tokens.append((r[0], m.group()))
                s = s[len(m.group()):]
                continue

    return tokens

def filter_whitespace(tokens):
    return list(filter(lambda x: x[0] != 'whitespace', tokens))

def print_tokens(tokens):
    for t in tokens:
        print(t)

if __name__ == '__main__':
    for t in tokenize('34 - (IV - asdasd?)'):
        print(t)

