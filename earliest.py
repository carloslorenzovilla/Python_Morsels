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
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)
