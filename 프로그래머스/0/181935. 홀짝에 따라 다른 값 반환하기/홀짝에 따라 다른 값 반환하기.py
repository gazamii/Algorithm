def solution(n):
    sum=0
    if n%2==1:
        for x in range(0,n+1) :
            if x%2==1:
                sum+=x
                
    elif n%2==0:
        for x in range(0,n+1) :
            if x%2==0:
                x=x**2
                sum+=x
            
    return sum