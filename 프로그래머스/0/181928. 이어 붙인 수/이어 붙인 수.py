def solution(num_list):
    x=''
    y=''
    for a in num_list:
        if a%2:
            x+=str(a)
        else:
            y+=str(a)
            
    return int(x)+int(y)
    
    