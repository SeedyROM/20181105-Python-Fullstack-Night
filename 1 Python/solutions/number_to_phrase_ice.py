ONES = dict(zip(range(10), ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
TENS = dict(zip(range(10), ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']))
TEENS = dict(zip(range(10, 20), ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']))

def number_to_phrase(num):
    original_num = num
    tens_digit = num % 100 // 10
    ones_digit = num % 10
    prefix = ''
    phrase = ''

    if num > 999999:
        return 'Invalid number. Enter number between 0 and 1 million.'

    if num > 9999:
        prefix = number_to_phrase(num // 1000)
        prefix = f'{prefix} thousand '
        num = num % 1000

    if num >= 1000:
        thousands_digit = num // 1000
        phrase += f'{ONES[thousands_digit]} thousand '

    if num >= 100:
        hundreds_digit = num % 1000 // 100
        phrase +=  f'{ONES[hundreds_digit]} hundred '
    
    if tens_digit > 1:
        phrase += TENS[tens_digit]
        if tens_digit and ones_digit:
            phrase += '-'
        if ones_digit:
            phrase += ONES[ones_digit]
    elif tens_digit == 1:
        teen = num % 100
        phrase += TEENS[teen]
    else:
    # elif tens_digit == 0: # equivalent to else
        if original_num == 0:
            return 'zero'
        phrase += ONES[ones_digit]

    
    return prefix + phrase


def main():
    while True:
        user_in = input("Enter a number to convert it to English, or 'x' to exit: ")
        if user_in in ['x', 'exit']:
            break
        print(number_to_phrase(int(user_in)))

main()