def solution(arr, queries):
    for q in queries:
        i=q[0]
        j=q[1]
        arr[i], arr[j]=arr[j], arr[i]
    return arr
        