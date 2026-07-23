def solution(intStrs, k, s, l):
    num=0
    result=[]
    for x in intStrs:
        num = int(x[s:s+l])
        if num>k:
            result.append(num)
    return result
