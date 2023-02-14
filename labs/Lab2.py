def total_time (cableLength_KM, packetLength_b):
    cable_speed_KMS = 200000
    data_rate = 10 * 1000000000 # bps
    
    transmittion_delay = packetLength_b/data_rate
    
    propagation_delay = cableLength_KM/cable_speed_KMS
    
    return transmittion_delay + (propagation_delay * 1000)
    
print ("{:.4f}".format(total_time(10000, 8000)))

# Q17
def transmission_delay (packetLength_bytes, rate_bps):
    packetLength_bit = packetLength_bytes * 8
    return packetLength_bit/rate_bps

# Q18
packetLength_bytes = 1000
rate_bps = 10000000

# Q19
packetLength_bytes = 1000
rate_bps = 10000000000
print(transmission_delay (packetLength_bytes, rate_bps) * 1000)

# Q21

def queueing_delay (rate_bps, numPackets, packetLength_b):
    return packetLength_b/rate_bps * numPackets

# Q22
rate_bps = 100 * 1000000
numPackets = 20
packetLength_b = 1500 * 8
print(queueing_delay (rate_bps, numPackets, packetLength_b) * 1000)

# Q29
def avg_trials_from_ber (bit_error_probability, packetLength_b):
    return 1/(1-(1- (1-bit_error_probability)**packetLength_b))

# Q30
bit_error_probability = 0.005
packetLength_b = 1000

# Q31
bit_error_probability = 0.001
packetLength_b = 2000

print(avg_trials_from_ber (bit_error_probability, packetLength_b))