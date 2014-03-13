__author__ = 'jingyuan'
# encoding=utf8
import datetime


def checkio(data):
    #replace this for solution
    _type = int(data[1:2], 16) >> 2
    year = int("20" + data[3] + data[2])
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
    DATEFORMAT = "%d %b %Y %H:%M:%S GMT %z"
    dt = datetime.datetime(year, month, day, hour, minute, second)
    p1 = dt.strftime(DATEFORMAT) + sign + str(timezone)
    length = int(data[16:18], 16)
    p2 = length
    offset = 18
    clist = []
    for i in range(length):
        c = 0
        if _type == 2:
            # print data[offset+2:offset+4] + data[offset:offset+2]
            c = int(data[offset:offset+4], 16)
            offset += 4
        elif _type == 1:
            # print data[offset:offset+2]
            c = int(data[offset:offset+2], 16)
            offset += 2
        elif _type == 0:
            # print data[offset:offset+2]
            c = int(data[offset:offset+2], 16) & 127
            offset += 2
        print c
        clist.append(unichr(c))
    p3 = ''.join(clist)
    print [p1, p2, p3.encode('utf-8')]
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
