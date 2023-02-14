def encodedate (day, month, year):
    
    if day > 31 or month > 12 or day <= 0 or month <= 0:
        return -1
    
    d = (day-1) << 23
    m = (month-1) << 28
    
    md = d | m
    
    mdy = md | year
    
    return mdy

def decodedate (x):
    
    month_bin = x & 0xF0000000
    month = (month_bin >> 28) + 1
    
    day_bin = x & 0x0F800000
    day = (day_bin >> 23) + 1
    
    year = (x & 0x007FFFFF) 
    
    return str(day) + '.' + str(month) + '.' + str(year)
    
    
def hexstring (x):    
    if type(x) != int:
        return -1
    
    if not x >= 0:
        return -2
    
    else:
        return find_hex(x)

def find_hex(x):
    hex_list = convert (x, 16)
    
    mapping = ['A', 'B', 'C', 'D', 'E', 'F']
    result = '0x'
    for i in hex_list:
        
        if i > 9:
            result += mapping[i-10]
        else:
            result += str(i)
            
    return result 

def convert (x, base):
    """ converts decimal -> binary """
    if type(x) != int:
        return -1
    
    if type(base) != int:
        return -2
    
    if not x >= 0:
        return -3
    
    if not base >= 2:
        return -4    
    
    else:
        return find_coefficients(x, base)

def find_coefficients(x, base):
    
    n = len(str(x)) - 1
    result = []
    while x > 0:
        remainder = x % base
        result.append(remainder)
        x = x // base
    result.reverse()
    return result  
 
