"""
This is a program simulating the receiver side of GBN,
******************
Input packets are formatted as
[seq_num, data]

Output packets are formatted as
[status, exp_num]
0 - an ACK is sent;
-1 - unexpected packets received; 
*******************
"""

def GBN_Receiver(packet,exp_num):
    """
    1. packet in form [seq_num, data]"""
    
    seq_num, data = packet
    #If the packet the receiver receives is in order, 
    #the receiver sends an ACK for the packet, delivers the data to the upper layer. 
    
    #In all other cases, 
    #the receiver discards the packet and resends an ACK for the most recently received in-order packet. 
    
    if seq_num == exp_num:
        status = 0
        exp_num += 1
    else:
        status = -1

    return [status, exp_num]

    
       
#Do NOT modify the following code    
def rcvr_test(packet_list):    
    action_list = []
    exp_num = 1
    
    for packet in packet_list:        
        action = GBN_Receiver(packet,exp_num)
        exp_num = action[1]
        action_list.append(action)    
        
    print(f'{action_list}')  
    
rcvr_test([[1,1]])
rcvr_test([[1,1],[2,2]])
rcvr_test([[1,1],[2,2],[3,3]])
rcvr_test([[0,1]])