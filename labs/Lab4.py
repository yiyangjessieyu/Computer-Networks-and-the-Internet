import math 

def last_fragment_size (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    
    total_fragments = math.floor(s/(m-o)) #rounds a number down to the next largest integer.
    last_packet_size = s - ((total_fragments) * (m-o))

    return last_packet_size + o

print (last_fragment_size(10000, 20, 1500))


def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    
    total_packages = math.ceil(s/(m-o)) #rounds a number up to the next largest integer.
    total_O = total_packages * o

    return total_packages  

print (number_fragments(10000, 20, 1500))


