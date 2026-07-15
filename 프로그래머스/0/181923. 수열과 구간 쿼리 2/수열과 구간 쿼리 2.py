def solution(arr, queries):
    real=0
    result=[]
    for a,b,c in queries:
        fake=[]
        for i in range(a, b+1):
            if arr[i]>c:
                fake.append(arr[i])
            
        if fake==[]:
            result.append(-1)
        else:
            real=min(fake)
            result.append(real)
            
    return result