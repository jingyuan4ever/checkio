__author__ = 'jingyuan'
import re
def checkio(text):
    """
        find all IPs
    """
    ret = []
    data = text.split(' ')
    regexp = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    for ip in data:
        if re.match(regexp, ip):
            flag = True
            for n in ip.split('.'):
                if int(n) not in range(0, 256):
                    flag = False
            if flag:
                ret.append(ip)
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("192.168.1.1 and 10.0.0.1 or 127.0.0.1") == \
        ["192.168.1.1", "10.0.0.1", "127.0.0.1"], "All correct"
    assert checkio("10.0.0.1.1 but 127.0.0.256 1.1.1.1") == \
        ["1.1.1.1"], "Only 1.1.1.1"
    assert checkio("167.11.0.0 1.2.3.255 192,168,1,1") == \
        ["167.11.0.0", "1.2.3.255"], "0 and 255"
    assert checkio("267.11.0.0 1.2.3.4/16 192:168:1:1") == \
        [], "I don't see IP"
    assert checkio("00250.00001.0000002.1 251.1.2.1") == \
        ["251.1.2.1"], "Be careful with zeros"
