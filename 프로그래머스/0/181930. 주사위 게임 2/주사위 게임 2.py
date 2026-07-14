def solution(a, b, c):
    x=len(set([a,b,c]))
    if x==3:
        return a+b+c
    elif x==1:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif x==2:
        return (a+b+c)*(a**2+b**2+c**2)
    