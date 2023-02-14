import math
def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b #not necessarily an integer multiple of S.

    total_packages = messageLength_b/maxUserDataBitsPerPacket_b
    total_O = total_packages * O

    if messageLength_b % maxUserDataBitsPerPacket_b != 0:
        return total_packages + total_O + O + (messageLength_b % maxUserDataBitsPerPacket_b)
    else:
        return total_packages + total_O 




print ("{:.1f}".format(total_number_bits(1000, 100, 10000)))
