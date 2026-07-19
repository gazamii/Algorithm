def solution(number):
    sum=0
    for a in number:
        sum+=int(a)
    return sum%9