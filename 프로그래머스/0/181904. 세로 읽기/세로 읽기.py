def solution(my_string, m, c):
    result=[]
    my_string=list(my_string)
    for x in range(c-1, len(my_string), m):
        result.append(my_string[x])
    return "".join(result)
    
    