
N= int(input())
l=[]

for i in range(N):
        entry=input().split()
        cmd=entry[0]
        
        if cmd=='pop':
            l.pop()
        
        elif cmd=='append':
            l.append(int(entry[1]))
         
        elif cmd =='insert':
            l.insert(int(entry[1]),int(entry[2]))
         
        elif cmd=='reverse':
            l.reverse()
            
        elif cmd=='sort':
            l.sort()   
         
        elif cmd=='remove':
            l.remove(int(entry[1]))   
             
        elif cmd=='print':
            print(l)