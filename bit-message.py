__author__ = 'jingyuan'
# encoding=utf8
import datetime


def checkio(data):
    #replace this for solution
    _type = int(data[1:2], 16) >> 2
    year = int(data[3] + data[2])
    if year > 69:
        year += 1900
    else:
        year += 2000
    month = int(data[5] + data[4])
    day = int(data[7] + data[6])
    hour = int(data[9] + data[8])
    minute = int(data[11] + data[10])
    second = int(data[13] + data[12])
    data15 = int(data[15], 16)
    sign = "+"
    if data15 / 8 == 1:
        sign = "-"
    timezone = int(str(data15 % 8) + data[14]) * 15 / 60
    if timezone == 0:
        sign = "+"
    DATEFORMAT = "%d %b %Y %H:%M:%S GMT %z"
    dt = datetime.datetime(year, month, day, hour, minute, second)
    p1 = dt.strftime(DATEFORMAT) + sign + str(timezone)
    length = int(data[16:18], 16)
    p2 = length
    offset = 18
    tmp = []
    rest = data[offset:]
    for i in range((len(rest) + 1) / 2):
        tmp.append(rest[i * 2:i * 2 + 2])
    tmp.reverse()
    rest = ''.join(tmp)
    clist = []
    stream = bin(int(rest, 16))[2::]
    step = 16
    if _type == 0:
        step = 7
    elif _type == 1:
        step = 8
    stream = '0' * (length * step - len(stream)) + stream
    for i in range(length):
        s = stream[len(stream) - (i + 1) * step:len(stream) - i * step]
        if _type == 2:
            s = s[8:] + s[:8]
        clist.append(unichr(int(s, 2)))

    p3 = ''.join(clist)
    return [p1, p2, p3]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(u'002080629173148007EDF27C1E3E9701') ==
            ['26 Aug 2002 19:37:41 GMT +2', 7, u'message']), "First Test"

    assert (checkio(u'00317050201171820FD3323BDC0ED341C4303DEC3E8700') ==
            ['05 Jul 2013 02:11:17 GMT +7', 15, u'Selamat Datang!']), "Second Test, 7 bit"

    assert (checkio(u'000130925161956915C8729E054A82C26D50DA0D7296EFA0EC5BBE06') ==
            ['29 Mar 2010 15:16:59 GMT -4', 21, u'Hey, I am in New York']), "Third Test, negative timezone"

    assert (checkio(
        u'08071010101010611F04180441043A043B044E04470435043D043804350020043F043E04340442043204350440043604340430043504420020043F0440043004320438043B043E') ==
            ['01 Jan 1970 01:01:01 GMT +4', 31,
             u'Исключение подтверждает правило']), "Fourth Test, simulate 32-bit signed integer real life problem"

    assert (checkio(
        u'088310913041804C23805E4E0D82E5805E4E4B002C805E4E4B4E0D82E5898B4E4B002C898B4E4B4E0D82E577E54E4B002C77E54E4B4E0D82E5884C4E4B002C5B7881F365BC884C4E4B800C6B6277E3 ') ==
            ['19 Jan 2038 03:14:08 GMT -11', 35, u'聞不若聞之,聞之不若見之,見之不若知之,知之不若行之,學至於行之而止矣']), "But, we pass Y2K38 problem"
