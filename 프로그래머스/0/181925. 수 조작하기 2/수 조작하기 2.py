def solution(nl):
    i=0
    str1=''
    for i in range(len(nl)-1):
        a=nl[i+1]-nl[i]
        key=dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
        str1+=key[a]
    return str1