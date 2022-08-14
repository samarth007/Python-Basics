

def SwapCase(s):
    reslt=[]
    for i in s:
        if i==i.lower():
            reslt.append(i.upper())
        else:
            reslt.append(i.lower())
    
    return ''.join(reslt)

print(SwapCase('HeLlo'))   
