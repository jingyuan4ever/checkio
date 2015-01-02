from datetime import datetime, timedelta
def broken_clock(starting_time, wrong_time, error_description):
    format = '%H:%M:%S'
    td = datetime.strptime(wrong_time,format)-datetime.strptime(starting_time, format)
    desc = error_description.split(' ')
    mis, misUnit, real, realUnit = int(desc[0]), desc[1].rstrip('s'), int(desc[3]), desc[4].rstrip('s')
    tdm = eval('timedelta(%ss=%d)'%(misUnit,mis))
    tdr = eval('timedelta(%ss=%d)'%(realUnit,real))
    realtime = td*int(tdr.total_seconds())/int(tdr.total_seconds()+tdm.total_seconds())+datetime.strptime(starting_time, format)
    return realtime.strftime(format)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
