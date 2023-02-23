ROMAN_NUMERAL_MAP = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def int_to_roman(num: int) -> str:
    if not isinstance(num, int) or num < 1 or num > 3999:
        raise ValueError("Input must be an integer between 1 and 3999.")
    roman_numeral = ''
    for value, numeral in ROMAN_NUMERAL_MAP:
        while num >= value:
            roman_numeral += numeral
            num -= value
    return roman_numeral

try:
    num = int(input("Enter a number between 1 and 3999: "))
    roman_numeral = int_to_roman(num)
    print(f"The Roman numeral for {num} is {roman_numeral}.")
except ValueError as e:
    print(e)
