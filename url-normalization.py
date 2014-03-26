__author__ = 'jingyuan'
import re

r = dict()
for i in range(0x41, 0x5A + 1):
    r[i] = chr(ord('a') + i - 0x41)
for i in range(0x61, 0x7A + 1):
    r[i] = chr(ord('a') + i - 0x61)
for i in range(0x30, 0x39 + 1):
    r[i] = str(i-0x30)
r[0x2d] = '-'
r[0x2e] = '.'
r[0x5f] = '_'
r[0x7e] = '~'


def trans(m):
    num = int(m.group()[1:], 16)
    if num in r.keys():
        return r[num]
    else:
        return m.group().upper()


def normalize(s):
    if len(s) == 0:
        return s
    pattern = '%\w{2}'
    return re.sub(pattern, trans, s)


def checkio(url):
    p = url.lower().split('/', 3)
    ret = 'http://'
    print p
    if p[2].split(':')[-1] == '80':
        ret += p[2].split(':')[0]
    else:
        ret += p[2]
    if len(p) == 3:
        return ret

    l = []
    ret += '/'
    for i in p[3].split('/'):
        if i == '.':
            continue
        elif i == '..':
            l.pop(-1)
        else:
            l.append(normalize(i))
    path = '/'.join(l)
    ret += path
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Http://Www.Checkio.org") ==\
           "http://www.checkio.org", "1st rule"
    assert checkio(u"http://www.checkio.org/%cc%b1bac") ==\
           "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio(u"http://www.checkio.org/task%5F%31") ==\
           "http://www.checkio.org/task_1", "3rd rule"
    assert checkio(u"http://www.checkio.org:80/home/") ==\
           "http://www.checkio.org/home/", "4th rule"
    assert checkio(u"http://www.checkio.org:8080/home/") ==\
           "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio(u"http://www.checkio.org/task/./1/../2/././name") ==\
           "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
