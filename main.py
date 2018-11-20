def q1(tape,index):
    if tape[index]=='':
        q1(tape,index+1)
    else:
        q2(tape,index+1)

def q2(tape,index):
    if tape[index]=='+':
        q3(tape,index+1)
    elif tape[index]=='-':
        q3(tape,index+1)
    else:
        q2(tape,index+1)

def q3(tape,index):
    if tape[index]=='1':
        q4(tape,index-1)
    elif tape[index]=='2':
        q5(tape,index-1)
    else:
        print (''.join(tape))

def q4(tape,index):
    if tape[index]=='-':
        q8(tape,index-1)
    else:
        q6(tape,index-1)
    
    
def q5(tape,index):
    if tape[index]=='-':
        q11(tape,index-1)
    else:
        q10(tape,index-1)
        
        
def q6(tape,index):
    if tape[index]=='0':
        tape[index]='1'
    elif tape[index]=='1':
        tape[index]='2'
    elif tape[index]=='2':
        tape[index]='0'
        q7(tape,index-1)
    else:
        q7(tape,index)
def q7(tape,index):
    if tape[index]=='0':
        tape[index]='1'
    elif tape[index]=='1':
        tape[index]='2'
    elif tape[index]=='2':
        tape[index]='0'
        q7(tape,index-1)
    else:
        tape[index]='1'
def q8(tape,index):
    if tape[index]=='0':
        tape[index]='2'
        q9(tape,index-1)
    elif tape[index]=='2':
        tape[index]='1'
    else:
        tape[index]='0'
        
        
def q9(tape,index):
    if tape[index]=='0':
        tape[index]='2'
        q9(tape,index-1)
    elif tape[index]=='1':
        tape[index]='0'
        q9(tape,index-1)
    elif tape[index]=='2':
        tape[index]='1'
    else:
       q12(tape,index)
       
def q10(tape,index):
    if (tape[index]!=' ')and(tape[index]!='0'):
        tape[index] =str(int(tape[index])-1)
        q6(tape,index-1)
    elif tape[index]=='0':
        tape[index]='2'
def q11(tape,index):
    if tape[index]=='0':
        tape[index]='1'
        q8(tape,index-1)
    elif tape[index]=='1':
        tape[index]='2'
        q8(tape,index-1)
    else:
        tape[index]='0'
        q12(tape,index-1)
        
        
def q12(tape,index):
    if tape[index]==' ':
        q13(tape,index+1)
def q13(tape,index):
    if tape[index]=='0':
       tape[index]=' '
       
tape =list(input())
q1(tape,0)
print(''.join(tape))
