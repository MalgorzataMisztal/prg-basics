def time_string(hours, minutes, time_format):
    minutes_str= f'{minutes:02d}'
    
    if time_format == '24': 
        hours_str = f'{hours:02d}'
        return hours_str + ':' + minutes_str
    
    elif time_format == '12':

        if hours <= 11:
            return hours + ':' + minutes + 'am'
        elif hours > 12:
            hours = hours - 12
            return hours + ':' + minutes + 'pm'
        elif hours == 0:
            hours = 12
            return hours + ':' + minutes + 'am'
        elif hours == 12:
            return hours + ':' + minutes + 'pm'
    else:
        return 'Invalid format'


time_string(15, 38, '24')
time_string(8, 3, '24')
time_string(0, 5, '24')
time_string(11, 15, '12')
time_string(0, 7, '12')
time_string(7, 30, '12')
time_string(12, 46, '12')
time_string(13, 10, '12')
time_string(19, 2, '12')