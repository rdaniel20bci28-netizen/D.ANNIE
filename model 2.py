def compress_string(S):
    if not S:
        return ""
    
    res = []
    count = 1
    
    for i in range(len(S) - 1):
        if S[i] == S[i+1]:
            count += 1
        else:
            res.append(S[i] + str(count))
            count = 1
            
    res.append(S[-1] + str(count))
    
    return "".join(res)
