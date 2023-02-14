import math

def packet_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b):
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    
    p_delay = L/C
    t_delay = (S+O)/R
    
    return (p_delay + t_delay + P) * 2

def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    
    p_delay = l/c
    t_delay = (s+o)/r
    
    total_packages = (m/s)
    
    return p_delay + t_delay + p + p_delay + (total_packages * t_delay) + p

print ("{}".format(total_transfer_time (10000, 200000, 0.001, 1000000, 1000, 100, 1000000000)))


