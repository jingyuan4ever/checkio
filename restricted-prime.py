__author__ = 'jingyuan'


def checkio(number):
    one = int(True)
    two = one + one
    chushu = two
    while chushu < number:
        total = int(False)
        while total <= number:
            total += chushu
            if total == number:
                return False
        chushu += one
    return True


assert checkio(2)
assert checkio(3)
