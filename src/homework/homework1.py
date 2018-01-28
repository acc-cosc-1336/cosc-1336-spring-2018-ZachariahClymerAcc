#given seconds, return time since midnight in hours, minutes, seconds

def get_hours_since_midnight(seconds):
    return (secons // 3600)

def get_minutes(seconds):

    return (seconds - (get_hours_since_midnight (seconds) *3 600)) // 60

def get_seconds(seconds):

    return seconds - ((get_hours_since_midnight(seconds) * 3600) + (get_minutes(seconds) * 60))
def time(): 
    seconds = 3800 
    print ('Total time since midnight in hh:mm:ss is ', get_hours_since_midnight(seconds), ':', get_minutes(seconds), ':', get_seconds(seconds) )
    
time()
