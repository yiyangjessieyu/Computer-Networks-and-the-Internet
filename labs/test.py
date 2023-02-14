# Q5
import math
def fragmentOffsets (fragmentSize_bytes, overheadSize_bytes, messageSize_bytes):
    """Please write a Python function which takes as parameters the values for the maximum frame size F, the per-frame overhead O, and the overall message size M, and which returns a list containing the (value of the) offset field of the first fragment, the offset field of the second fragment, and so on."""
    F  =  fragmentSize_bytes
    O  =  overheadSize_bytes
    M  =  messageSize_bytes
    
    result = []
    
    payload = F - O
    
    frag_n = math.ceil(M/payload)
    
    index = 0
    for i in range(0, frag_n):
        result.append(index)
        index += payload
    
    return result
    
#print(fragmentOffsets(1500,40,3000)==[0,1460,2920])

# Q6
def queueingDelay (packetSize_bits, dataRate_bps, flagCurrentTransmission, numberInQueue):
    L    =  packetSize_bits
    R    =  dataRate_bps
    flag =  flagCurrentTransmission
    N    =  numberInQueue
    
    result = 0
    
    if flag == True:
        result = ((L/R) * N) + ((L/R)/2)
    #else:
        #return N * (L/R)
    
    return result
    
#print(queueingDelay(1000,1000000,True,0))
#print(abs(queueingDelay(1000,1000000,True,0)-0.0005)<0.00001)
#print(queueingDelay(1000,1000000,False,0))
#print(abs(queueingDelay(1000,1000000,False,0)-0.0000)<0.00001)

# Q19:
def packetSwitching (numberRouters, messageSize_b, userDataSize_b, overheadSize_b, processingTime_s, dataRate_bps, propagationDelay_s):
    N  =  numberRouters
    M  =  messageSize_b
    S  =  userDataSize_b
    O  =  overheadSize_b
    P  =  processingTime_s
    R  =  dataRate_bps
    T  =  propagationDelay_s

#print(abs(packetSwitching(3, 10000, 1000, 100, 0.001, 1000000, 0.02)-0.0973)<0.0001)

# Q8
def IPToString (addr):
    
    first = (addr & 0xFF000000) >> 24
    sec = (addr & 0x00FF0000) >> 16
    third = (addr & 0x0000FF00) >> 8
    fourth = (addr & 0x000000FF)
    
    result = str(first) + "." + str(sec) + "." + str(third) + "." + str(fourth)
    return(result)
    
print(IPToString(0x20304050))
