def RDT_Receiver(packet):
    #Your code here:
    
    seq_num, data = packet
    
    if seq_num != 0 and seq_num != 1:
        status = -1
        seq_num = -1
    
    else: #valid packet, sends back ACK
        status = 0
    
    return [status, seq_num]
       
 



#Do NOT modify the following lines    
def rcvr_test(packet_list):    
    action_list = []    
    
    for packet in packet_list:        
        action = RDT_Receiver(packet)
        action_list.append(action)    
        
    print(f'{action_list}')  

rcvr_test([[0, 1], [2, 1],[0, 2],[1, 3],[0, 4]])
