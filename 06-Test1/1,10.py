def f(time1, time2):
    if 'am' in time1 or 'am' in time2:
        time1.replace('am', '')
        time2.replace('am', '')
        