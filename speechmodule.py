__author__ = 'jingyuan'

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number == 0:
        return FIRST_TEN[0]
    units = number%10
    number/=10
    decades = number%10
    number/=10
    hundreds = number%10
    strList = []
    if hundreds!=0:
        strList.append(FIRST_TEN[hundreds])
        strList.append(HUNDRED)
    if decades == 0:
        strList.append(FIRST_TEN[units])
    elif decades == 1:
        strList.append(SECOND_TEN[units])
    else:
        strList.append(OTHER_TENS[decades-2])
        if units != 0:
            strList.append(FIRST_TEN[units])
    return ' '.join(strList)

#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
