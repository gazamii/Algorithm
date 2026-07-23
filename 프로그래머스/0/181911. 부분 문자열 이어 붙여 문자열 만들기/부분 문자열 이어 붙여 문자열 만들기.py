def solution(my_strings, parts):
    result=[]
    for x,(a,b) in zip(my_strings,parts):
        result.append(x[a:b+1])
    return "".join(result)
            