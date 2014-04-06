__author__ = 'jingyuan'
import time
def formatURI(uri):
    domain = uri.split('/')[2]
    parts = domain.split('.')
    if len(parts) != 2:
        parts.pop(0)
    return '.'.join(parts).lower()


class record:
    def __init__(self, string):
        parts = string.split(';;')
        self.t = time.mktime(time.strptime(parts[0], '%Y-%m-%d-%H-%M-%S'))
        self.u = parts[1].lower()
        self.d = formatURI(parts[2])
        print 'new record: %s, %s, %s' % (self.t, self.u, self.d)

    def __cmp__(self, other):
        return self.t - other.t

    def __str__(self):
        return 'record: %s, %s, %s' % (self.t, self.u, self.d)


class session:
    def __init__(self, rec):
        self.u = rec.u
        self.d = rec.d
        self.f = rec.t
        self.l = rec.t
        self.c = 1

    def isIn(self, rec):
        if rec.u == self.u and rec.d == self.d and rec.t < self.l+1800:
            return True
        return False

    def update(self, rec):
        self.l = rec.t
        self.c += 1

    def __str__(self):
        return "%s;;%s;;%d;;%d" % (self.u, self.d, int(self.l-self.f)+1, self.c)

    def __cmp__(self, other):
        if self.u != other.u:
            return cmp(self.u, other.u)
        if self.d != other.d:
            return cmp(self.d, other.d)
        d1 = int(self.l-self.f)+1
        d2 = int(other.l-other.f)+1
        if d1 != d2:
            return cmp(d1, d2)
        return cmp(self.c, other.c)


class sessionController:
    def __init__(self):
        self.sl = []
        print "session controller started."

    def insert(self, rec):
        for s in self.sl:
            if s.isIn(rec):
                s.update(rec)
                print "session updated"
                return
        self.sl.append(session(rec))
        print "new session"

    def __str__(self):
        self.sl.sort()
        return '\n'.join([str(i) for i in self.sl])


def checkio(log_text):
    sc = sessionController()
    recordList = []
    for line in log_text.split('\n'):
        recordList.append(record(line))
    recordList.sort()
    for i in recordList:
        sc.insert(i)
    return str(sc)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
"""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
==
"""name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"
