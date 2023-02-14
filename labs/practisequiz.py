
def packeterrorprobability (pktLength_b, bitErrorProb):
    L = pktLength_b
    P = bitErrorProb
    
    return 1 - (1-P)**L
    
# Question 3: True
# print (abs(packeterrorprobability(1000, 0.001)-0.6323)<0.0001)
# print (abs(packeterrorprobability(1000, 0.0001)-0.0951)<0.0001)

# Q4: 0.181
# print (packeterrorprobability(2000, 0.0001))

def twowrongbits (pktLength_b, bitErrorProb):
    L = pktLength_b
    P = bitErrorProb
    return 1 - ((1-P)**(L) + (P*L * (1-P)**(L-1)))

# Q5: True
# print (abs(twowrongbits(1000, 0.001)-0.2642)<0.0001)

def propagation_delay (numberSwitches, cableLength_km, speedOfLight_kms):
    "Please work out a general expression for the total combined propagation delay that all call-setup-request and call-setup-response messages cause."
    N     = numberSwitches
    L     = cableLength_km
    C     = speedOfLight_kms

    prop_delay = L / C
    
    prop_delay_A_B = prop_delay * (N + 1)
    
    return prop_delay_A_B * 2

# Q6: True
# print (abs(propagation_delay(3, 7500, 200000)-0.3)<0.0001)

def transmission_delay (numberSwitches, dataRate_bps, messageLengthRequest_b, messageLengthResponse_b):
    """total combined transmission delay of all call-setup-request and call-setup-response transmissions """
    N     = numberSwitches
    R     = dataRate_bps
    Mreq  = messageLengthRequest_b
    Mresp = messageLengthResponse_b
    
    trans_delay_req = Mreq/R
    trans_delay_resp = Mresp/R
    
    trans_delay_req_A_B = trans_delay_req * (N+1)
    trans_delay_resp_A_B = trans_delay_resp * (N+1)
    
    return trans_delay_req_A_B + trans_delay_resp_A_B
    
# Q7: True
# print (abs(transmission_delay(3, 10000000, 2000, 1000)-0.0012)<0.0001)

def processing_delay (numberSwitches, processingTimes_s):
    """combined total processing delay incurred for the processing of all call-setup-request and call-setup-response transmissions"""
    N     = numberSwitches
    P     = processingTimes_s
    
    return P * (N+1) * 2
    
# Q8: True
# print (abs(processing_delay(3, 0.001)-0.008)<0.0001)

def connection_setup_delay (numberSwitches, cableLength_km, speedOfLight_kms, dataRate_bps, messageLengthRequest_b, messageLengthResponse_b, processingTimes_s):
    """expression for the call-setup delay 
    (i.e. the time between A starting to transmit the call-setup-request message 
    and A finishing receiving and processing the call-setup-response message)"""
    
    N     = numberSwitches
    L     = cableLength_km
    C     = speedOfLight_kms
    R     = dataRate_bps
    Mreq  = messageLengthRequest_b
    Mresp = messageLengthResponse_b
    P     = processingTimes_s
    
    prop_delay = L/C
    trans_delay_req = Mreq/R
    trans_delay_resp = Mresp/R 
    
    req_time_in_s = (prop_delay + trans_delay_req + P) * (N+1)
    resp_time_in_s = (prop_delay + trans_delay_resp + P) * (N+1)
    
    call_set_up_delay = req_time_in_s + resp_time_in_s
    
    return call_set_up_delay

# Q9: True
# print (abs(connection_setup_delay(3, 7500, 200000, 10000000, 2000, 1000, 0.001)-0.3092)<0.0001)

# Q10: 0.24530000000000002
# numberSwitches = 10 
# cableLength_km = 2000 
# speedOfLight_kms = 200000
# dataRate_bps = 10000000 
# messageLengthRequest_b =2000
# messageLengthResponse_b =1000
# processingTimes_s = 0.001
# print (connection_setup_delay (numberSwitches, cableLength_km, speedOfLight_kms, dataRate_bps, messageLengthRequest_b, messageLengthResponse_b, processingTimes_s))
bitmasks = [0b00000000000000000000000000000000,

            0b10000000000000000000000000000000,

            0b11000000000000000000000000000000,

            0b11100000000000000000000000000000,

            0b11110000000000000000000000000000,

            0b11111000000000000000000000000000,

            0b11111100000000000000000000000000,

            0b11111110000000000000000000000000,

            0b11111111000000000000000000000000,

            0b11111111100000000000000000000000,

            0b11111111110000000000000000000000,

            0b11111111111000000000000000000000,

            0b11111111111100000000000000000000,

            0b11111111111110000000000000000000,

            0b11111111111111000000000000000000,

            0b11111111111111100000000000000000,

            0b11111111111111110000000000000000,

            0b11111111111111111000000000000000,

            0b11111111111111111100000000000000,

            0b11111111111111111110000000000000,

            0b11111111111111111111000000000000,

            0b11111111111111111111100000000000,

            0b11111111111111111111110000000000,

            0b11111111111111111111111000000000,

            0b11111111111111111111111100000000,

            0b11111111111111111111111110000000,

            0b11111111111111111111111111000000,

            0b11111111111111111111111111100000,

            0b11111111111111111111111111110000,

            0b11111111111111111111111111111000,

            0b11111111111111111111111111111100,

            0b11111111111111111111111111111110,

            0b11111111111111111111111111111111]    

def ip2Int (dd):

    digits=dd.split('.')

    intIp=0

    cnt=0

    for num in reversed(digits):

        intIp += int(num) * 256 **(cnt)

        cnt +=1

    return intIp

def match (dst, netaddr, kbitmask):

    dest_masked = dst & kbitmask
    net_masked = netaddr & kbitmask
    
    return dest_masked == net_masked
    
# Q25: True
print (match(ip2Int("130.149.49.77"), ip2Int("130.149.0.0"), bitmasks[16]))
