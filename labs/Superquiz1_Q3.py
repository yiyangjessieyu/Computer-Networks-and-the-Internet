def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    
    # if version != 4:
        # return 1
    if hdrlen.bit_length() > 4 or hdrlen < 5:
        return 2
    if tosdscp.bit_length() > 6 or tosdscp < 0:
        return 3   
    # if totallength.bit_length() > 16 or totallength < 0:
        # return 4    
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
    
    headerchecksum = calculate_checksum(header_bytes, headerchecksum, optional_header)
    
    return packet

def calculate_checksum(header_bytes, headerchecksum, optional_header):
    # IPv4 header as consisting of ten consecutive 16-bit non-negative integer numbers
    # Add up these ten numbers, call the result X.
    
    n = header_bytes/2
    
    x = 0
    for i in range(0, header_bytes, 2):
        x += int((pkt[i] << 8) | pkt[i+1])
    
    while x > 0xFFFF:
        x0 = x & 0xFFFF
        x1 = x >> 16
        x = x0 + x1
        
    
    return x == 0xFFFF
    
def revisedcompose (hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    
    version = 4
    
    bytes_per_header = 4 # packet per header
    header_bytes = bytes_per_header * hdrlen # packet_length
        
    totallength = header_bytes + len(payload)
    
    optional_header = bytearray(header_bytes)
    
    headerchecksum = 0
    
    pkt = composepacket(version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress)
    
    return pkt
    
print(revisedcompose (6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])))
