

def SwapCase(s):
    reslt=[]
    for i in s:
        if i==i.lower():
            reslt.append(i.upper())
        else:
            reslt.append(i.lower())
    
    return ''.join(reslt)

print(SwapCase('HeLlo'))   
####################################################################
r='Heloo how are you'
strl=r.split(' ')
print('-'.join(strl))

####################################################################
#Inserting character in String
s='abcdefg'
l=[]
for i in s:
  l.append(i)
for i in range(len(l)):
    if i==2:
        l[i]='s'
        break
print(''.join(l))        

#####################################################################
#Number of times substring present in original string
word='abcdcdcd'
sub='cdc'
n=0
for i in range(len(word)):
    if word[i:].startswith(sub):
        n+=1
print(n)       