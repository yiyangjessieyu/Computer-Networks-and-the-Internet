import math
def number_fdma_channels (b_hz, g_hz, u_hz):
    """Suppose we have an overall system bandwidth of B Hz. 
    The bandwidth required for a guard band is G Hz and 
    the bandwidth required for one user channel (sub-channel) is U Hz"""
    
    N = math.floor(b_hz/(g_hz + u_hz))
    
    # Also works below
    N_channel_and_guard_hz = b_hz - g_hz
    N = math.floor(N_channel_and_guard_hz/ (g_hz + u_hz))    
    
    return N

# Q2: 
# Please find an expression for the maximum number N of users that can be accommodated in the system
print (number_fdma_channels(1000000, 200, 20000))

# Q3:
b_hz = 1 * 1000000
g_hz =  1 * 1000
u_hz = 30 * 1000
print (number_fdma_channels (b_hz, g_hz, u_hz))

import math
def number_tdma_users (s_s, g_s, u_s):
    """Suppose we are operating with TDMA using a superframe length of S seconds, 
    a guard time of G seconds, and 
    the length of a user slot is U seconds."""
    
    N = math.floor(s_s/(g_s + u_s))

    # Doesnt works below as superframe = s_s
    # N_channel_and_guard_s = s_s - g_s
    # N = math.floor(N_channel_and_guard_s/ (g_s + u_s))
    # N += 1
    
    return N
    

# Q4: maximum number of users that the system can support
print (number_tdma_users(1, 0.001, 0.008))
print (number_tdma_users(1.2, 0.002, 0.02))

# Q5:
s_s = 100 / 1000
g_s = 1 / 1000
u_s =  5 / 1000
print(number_tdma_users (s_s, g_s, u_s))

# Q5:
s_s = 100 / 1000
g_s = 1 / 1000
u_s =  5 / 1000
print(number_tdma_users (s_s, g_s, u_s))

def p_persistent_csma_collision_probability (p):
    return (1-p)/p

# Q12:
print ("{:.3f}".format(p_persistent_csma_collision_probability(0.2)))

#############################

def p_persistent_csma_access_delay (p):
    q = 1 - p
    return q/p
    
print ("{:.3f}".format(p_persistent_csma_access_delay(0.1)))



import math
def number_fdma_channels (b_hz, g_hz, u_hz):
    """Suppose we have an overall system bandwidth of B Hz. 
    The bandwidth required for a guard band is G Hz and 
    the bandwidth required for one user channel (sub-channel) is U Hz"""
    
    first_hz = g_hz + u_hz + g_hz
    
    N = math.ceil(b_hz/(g_hz+ u_hz))
    
    return N

# Q3: 
# Please find an expression for the maximum number N of users that can be accommodated in the system
print (number_fdma_channels(1000000, 200, 20000))