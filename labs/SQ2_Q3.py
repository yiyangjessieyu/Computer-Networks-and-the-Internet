"""
Sender side simulation of GBN;

An event is formatted as
[type, seq_num, data]
0 data to send; no check on seq_num and data;
1 ACK received; acking seq_num;
2 timeout event; resend all outgoing unAck'ed events; no check on seq_num and data;

Output of function GBN_sender() is formatted as
[status, base, next_seq]
-1 unexpected event/window full
0 data sent successfully
1 ACK processed; 
2 resending finished; 

N - the window size
base - seq# of lower winder boundary (base)

"""

N = 4 #window size;

def GBN_sender(event,base,next_seq):        
    if event[0] == 0: #Data to send; check whether the window is full;
        if event[1] < base + N: 
            return [0, base, next_seq + 1]
        else:
            return [-1, base, next_seq]
        
    if event[0] == 1: #ACK to process;
        if event[1] in range(base, next_seq):
            return [1, event[1] + 1 , next_seq]
        else:
            return [-1, base , next_seq]

    if event[0] == 2:#timeout event
        return [2, base, next_seq]      
                

#Do NOT modify the following code    
def sndr_test(event_list):    
    base = 0
    next_seq = 0
    action_list = []    
    
    for event in event_list:        
        action = GBN_sender(event,base,next_seq)
        base = action[1]
        next_seq = action[2]
        action_list.append(action)    
        
    print(f'{action_list}')    
    
sndr_test([[2,0,0]])
sndr_test([[0, 0, 1]])
sndr_test([[0, 0, 1], [0, 1, 2]])
sndr_test([[0, 0, 1], [0, 1, 2], [0, 2, 3]])
sndr_test([[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1,2,3],[0,4,5],[0,5,6],[2,0,0],[1,4,5]])