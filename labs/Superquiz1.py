def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    
    if version != 4:
        return 1
    if hdrlen.bit_length() > 4 or hdrlen < 0:
        return 2
    if tosdscp.bit_length() > 6 or tosdscp < 0:
        return 3   
    if totallength.bit_length() > 16 or totallength < 0:
        return 4    
    if identification.bit_length() > 16 or identification < 0:
        return 5   
    if flags.bit_length() > 3 or flags < 0:
        return 6    
    if fragmentoffset.bit_length() > 13 or fragmentoffset < 0:
        return 7    
    if timetolive.bit_length() > 8 or timetolive < 0:
        return 8    
    if protocoltype.bit_length() > 8 or protocoltype < 0:
        return 9    
    if headerchecksum.bit_length() > 16 or headerchecksum < 0:
        return 10       
    if sourceaddress.bit_length() > 32 or sourceaddress < 0:
        return 11   
    if destinationaddress.bit_length() > 32 or destinationaddress < 0:
        return 12    
    
    packet = bytearray(20)
    
    
    packet[0] = (version << 4) | (hdrlen)
    
    packet[1] = tosdscp
    
    packet[2] = (totallength & 0xFF00) >> 8
    packet[3] = totallength & 0x00FF
    
    packet[4] = (identification & 0xFF00) >> 8
    packet[5] = identification & 0x00FF 
    
    flag_stuff = (flags << 13) | (fragmentoffset)
    packet[6] = (flag_stuff & 0xFF00) >> 8
    packet[7] = flag_stuff & 0x00FF     
    
    packet[8] = timetolive
    
    packet[9] = protocoltype
    
    packet[10] = (headerchecksum & 0xFF00) >> 8
    packet[11] = headerchecksum & 0x00FF  
    
    packet[12] = (sourceaddress & 0xFF000000) >> 24
    packet[13] = (sourceaddress & 0x00FF0000) >> 16
    packet[14] = (sourceaddress & 0x0000FF00) >> 8
    packet[15] = sourceaddress & 0x000000FF     
    
    packet[16] = (destinationaddress & 0xFF000000) >> 24
    packet[17] = (destinationaddress & 0x00FF0000) >> 16
    packet[18] = (destinationaddress & 0x0000FF00) >> 8
    packet[19] = destinationaddress & 0x000000FF        
    
    return packet
    
def basicpacketcheck (pkt):
    
    if len(pkt) < 20:
        return 1
    elif (pkt[0] >> 4) != 4: # double check this!
        return 2
    elif verify_checksum_correct(pkt) == False:
        return 3
    elif pkt[3] != len(pkt):
        return 4
    else:
        return True

def verify_checksum_correct(pkt):
    # IPv4 header as consisting of ten consecutive 16-bit non-negative integer numbers
    # Add up these ten numbers, call the result X.
    
    x = 0
    for i in range(0, len(pkt), 2):
        x += int((pkt[i] << 8) | pkt[i+1])
        print(bin(x), "aaaaaaa", i)
    
    while x > 0xFFFF:
        x0 = x & 0xFFFF
        x1 = x >> 16
        x = x0 + x1
        
    return x == 0xFFFF
    
    
print(basicpacketcheck(bytearray ([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])))

pkt1 = bytearray ([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
pkt2 = bytearray ([0x45, 0x0, 0x0, 0x1e, 0x16, 0x2e, 0x0, 0x0, 0x40, 0x6, 0xcd, 0x59, 0x66, 0x66, 0x44, 0x44, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
pkt3 = bytearray ([0x45, 0x0, 0x0, 0x1b, 0x12, 0x67, 0x20, 0xe, 0x20, 0x6, 0x35, 0x58, 0x66, 0x66, 0x44, 0x44, 0x55, 0x44, 0x33, 0x22, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
print(basicpacketcheck(pkt3))