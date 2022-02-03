import time

def get_date():

    list = str(time.localtime(time.time())).split('=')
    types = ['year', 'month', 'day', 'hour', 'minute', 'second', 'week_day', 'year_day']
    date = {}

    for index, type in enumerate(types, 1):
        
        date[type] = list[index].split(',')[0]
        
    return date
        
def checkif_date(file):
    
    current_date = "{}-{}".format(get_date()['month'], get_date()['day'])
    
    with open(file, 'r') as f:
        
        date = f.read()
        
    with open(file, 'w') as f:
        
        f.write(current_date)
        
    if date == current_date:
        
        return True
    
    else:
        
        return False