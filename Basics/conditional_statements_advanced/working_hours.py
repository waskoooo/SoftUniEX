time_of_day = int(input())
day_of_week = input()

if time_of_day == 10 or \
    time_of_day == 11 or\
    time_of_day == 12 or\
    time_of_day == 13 or \
    time_of_day == 14 or \
    time_of_day == 15 or \
    time_of_day == 16 or \
    time_of_day == 17 or \
    time_of_day == 18:
    if day_of_week == 'Monday' or \
        day_of_week == 'Tuesday' or \
        day_of_week == 'Wednesday' or \
        day_of_week == 'Thursday' or \
        day_of_week == 'Friday' or \
        day_of_week == 'Saturday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
