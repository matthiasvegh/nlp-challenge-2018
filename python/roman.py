#!/usr/bin/env python3

def get_numerals():
    numerals = 'I:1 V:5 X:10 L:50 C:100 D:500 M:1000'.split()
    result = dict()
    for item in numerals:
        roman, value = item.split(':')
        value = int(value)
        result[roman] = value

    return result


def make_blocks(roman):
    result = []
    last_digit = None
    count = 0

    for digit in roman:
        if digit != last_digit:
            if last_digit:
                result.append((last_digit, count))
            last_digit = digit
            count = 0
        count += 1

    if last_digit:
        result.append((last_digit, count))

    return result


def value_blocks(bs):
    result = []
    ns = get_numerals()
    for (digit, count) in bs:
        digit_value = ns[digit]
        block_value = digit_value * count
        result.append((digit_value, block_value))
    return result


def is_descending(bs):
    last_value = None
    for digit_value, _ in bs:
        if last_value is None or digit_value < last_value:
            last_value = digit_value
            continue
        return False
    return True


def merge(vs):
    # for (digit_value, block_value) in vs:
    if len(vs) < 2:
        return vs

    for i in range(len(vs) - 1):
        d0, v0 = vs[i]
        d1, v1 = vs[i + 1]
        if d0 < d1:
            result = vs[:i] + [(d1, v1 - v0)] + vs[i + 2:]
            return result
    return vs


def from_roman(roman):
    bs = make_blocks(roman)
    vs = value_blocks(bs)
    while not is_descending(vs):
        size = len(vs)
        vs = merge(vs)
        if len(vs) == size:
            raise Exception('Something went wrong')

    total = 0
    for d, v in vs:
        total += v

    return total


def to_roman(value):
    result = ''
    ms = value // 1000
    value = value % 1000
    result += 'M' * ms

    if value >= 500:
        result += 'D'
        value -= 500

    if value >= 400:
        result += 'CD'
        value -= 400
    elif value >= 100:
        cs = value // 100
        result += 'C' * cs
        value = value % 100

    if value >= 90:
        result += 'XC'
        value -= 90
    elif value >= 50:
        result += 'L'
        value -= 50

    if value >= 40:
        result += 'XL'
        value -= 40
    elif value >= 10:
        xs = value // 10
        result += 'X' * xs
        value = value % 10


    vs = '- I II III IV V VI VII VIII IX'.split()
    assert value < 10, 'Invalid value: {}'.format(value)

    if value > 0:
        result += vs[value]

    return result




if __name__ == '__main__':
    print(to_roman(from_roman('LIX')))
