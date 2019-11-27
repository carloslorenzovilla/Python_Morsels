#I want you to write a function that takes two strings 
# representing dates and returns the string that represents 
# the earliest point in time. The strings are in the US-specific 
# MM/DD/YYYY format... just to make things harder. Note that the 
# month, year, and day will always be represented by 2, 4, and 2 
# digits respectively.

def get_earliest(*dates):
    """ Determines the earliest date in a sequence
    
        *dates: tuple of dates
        
        returns: string
    """
    older = dates[0]
    for i, (month, day, year) in enumerate((date.split('/') for date in dates)):     
        if year < older[-4:]:
            older = dates[i]
        if year == older[-4:] and month < older[0:2]:
            older = dates[i]
        if year == older[-4:] and month == older[0:2] and day < older[3:5]:
            older = dates[i]
    return older
