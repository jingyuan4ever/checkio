__author__ = 'jingyuan'


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    main = float(number)
    powerLength = len(powers)
    i = 0
    while abs(main) >= base and i < powerLength - 1:
        main /= base
        i += 1
    if decimals == 0:
        main = int(main)
    else:
        main = round(main, decimals)
    fmt = "%."+str(decimals)+"f"+powers[i]+suffix
    ret = fmt % main
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

