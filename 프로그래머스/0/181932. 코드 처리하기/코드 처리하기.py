def solution(code):
    mode=0
    ret=''
    i=0
    for x in code:
        if x=='1':
            mode=change(mode)
        else:
            if mode==0:
                if i%2==0:
                    ret+=code[i]
            elif mode==1:
                if i%2==1:
                    ret+=code[i]
        i+=1
    if ret=='':
        return 'EMPTY'
    return ret
            
def change(mode):
    if mode==0:
        mode=1
    elif mode==1:
        mode=0
    return mode