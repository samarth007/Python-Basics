

n,m=map(int,input().split())
l=[]

for i in range(n//2):
    design=((2*i+1)*'.|.').center(m,'-')
    print(design)
    l.append(design)

print('WELCOME'.center(m,'-'))
l.reverse()    
for i in range(n//2):
    print(l[i])

# for i in range(n//2):
#     for j in range(m):
#         print('-',end='')
#     print()    
# print('WELCOME'.center(m,'-'))
# for j in range(n//2):
#     for i in range(m):
#         print('-',end='')
#     print()        