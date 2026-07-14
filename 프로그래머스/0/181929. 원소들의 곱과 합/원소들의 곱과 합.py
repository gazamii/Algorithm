def solution(num_list):
    a=1
    b=0
    for x in num_list:
        a*=x
        b+=x
    if ((b**2)>a):
        return 1
    else:
         return 0
