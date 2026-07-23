def solution(my_string):
    result=[]
    for x in range(1,len(my_string)+1):
        result.append(my_string[-x:])
    return sorted(result)