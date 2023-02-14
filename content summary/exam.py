def GenACK(segments):
    segSize = 100
    
    last_result = segments[0]
    
    #the first segment is always in-order. 
    result = [last_result + segSize]
    recent_in_order = segments[0] + segSize
    
    for item in segments[1:]:
       # print(item, last_result)
        if item > last_result:
            
            recent_in_order = result[-1] + segSize          
            result.append(recent_in_order)
        else:
            result.append(recent_in_order)
        
    
        last_result = item
    
    return result

print(GenACK([1,101,201]))
print(GenACK([1]))
print(GenACK([1,101]))
print(GenACK([1,201,301]))
print(GenACK([1,201,101]))
print(GenACK([1,1]))