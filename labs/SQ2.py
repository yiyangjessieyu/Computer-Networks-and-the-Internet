"""
Sender side simulation of RDT 3.0;

Input packets are formatted
[type, seq_num, message]
0 message with seq_num to be send;
1 ACK received; acking seq_num;
2 timeout event; resend last packet; 

Output packets are formatted
[status, seq_num]
-1 unexpected packet, -1 as seq_num;
0 message sent successfully, seq_num is the seq # of the message;
1 ACK processed; seq_num is the ACk seq_num;
2 resending finished; seq_num is the seq_num of the resent message;

Four states as described in the FSM
0 - wait for data 0;
1 - wait for ack 0;
2 - wait for data 1;
3 - wait for ack 1;

"""

def RDT_sender(event,state):        
    #Adding your own code below
    
    event_type = event[0]
    
    if len(event) > 1:
        seq_num = event[1]     
        if len(event) > 2:
            data = event[2]
        
    has_error = False
        
    #Initial state; only accepts data 0; return error otherwise; 
    if state == 0:
        #Incoming of data with corresponding seq_num
        if event_type == 0 and seq_num == 0: 
            state = 1
            status = 0
        else:
            has_error = True
    
    #Wait for ACK 0
    elif state == 1:
        #ACK which acknowledges the reception of data with seq_num at the receiver side
        if event_type == 1 and seq_num == 0: 
            state = 2
            status = 1
        #Timeout
        elif event_type == 2:
            status = 2
            seq_num = 0
        else:
            has_error = True        

    #Wait for data 1
    elif state == 2:
        #Incoming of data with corresponding seq_num
        if event_type == 0 and seq_num == 1: 
            state = 3
            status = 0
        else:
            has_error = True        
    
    #Wait for ACK 1
    elif state == 3:
        #ACK which acknowledges the reception of data with seq_num at the receiver side
        if event_type == 1 and seq_num == 1: 
            state = 0
            status = 1
        #Timeout
        elif event_type == 2:
            status = 2
            seq_num = 1
        else:
            has_error = True        
     
    #Sender receives unexpected packet (event)       
    if has_error:
        status = -1  
        seq_num = -1
        
    return (state, [status, seq_num])


#Do not modify the following lines    
def sndr_test(event_list):    
    state = 0
    action_list = []    
    
    for event in event_list:   
        state, action = RDT_sender(event,state)
        action_list.append(action)   
    print(f'{action_list}')

sndr_test([[0, 0, 1], [1, 0, 1], [0, 1, 3], [2],[1,1,3]])
sndr_test([[0, 0, 1], [2, 0, 1]])
sndr_test([[0, 0, 1], [0, 1, 2], [0, 0, 3], [0, 1, 4], [0, 0, 5]])
sndr_test([[0, 0, 1], [1, 0, 1], [0, 1, 3], [1, 1, 3]])	
sndr_test([[0, 0, 1], [1, 0], [0, 1, 3], [1, 1]])
sndr_test([[0, 0, 1], [1, 1, 1], [0, 1, 3], [1, 1, 3]])
sndr_test([[0, 0, 1], [1, 0, 1], [0, 1, 3], [1, 1, 3],[0,1,4]])

