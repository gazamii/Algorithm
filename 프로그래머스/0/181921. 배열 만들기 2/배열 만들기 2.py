def solution(l, r):
    result=[]
    for x in range(l,r+1):
        x=str(x)
        ok=1    
        for b in x:
            if b=='0' or b=='5':
                ok=1
            else:
                ok=0
                break
        if ok==1:
            result.append(int(x))
            
    if not result:
        result.append(-1)
    return result
            