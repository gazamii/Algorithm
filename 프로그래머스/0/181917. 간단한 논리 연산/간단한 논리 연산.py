def solution(x1, x2, x3, x4):
    a=Set(x1, x2)
    b=Set(x3, x4)
    
    return True if a==b==True else False

def Set(x1, x2):
    set1=set([x1, x2])
    if len(set1)==1:
        if x1==True:
            return True
        else:
            return False
    else:
        return True