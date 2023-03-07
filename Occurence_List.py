
def occurence(lst):
  l=len(lst)
  vismap={}
  for i in range(l):
      c = 2
      if lst[i] not in vismap:
       for j in range(i+1,l):
          if lst[i]==lst[j]:
              vismap[lst[i]]=c
              c+=1
  return vismap

lst=[23,24,24,23,10,8,11,10,23,10,24,10,8]
d=occurence(lst)
print(d)
a=sorted(d.keys(),reverse=True)
print(a)
# for i in a:
#     print(i[0],end=' ')




# d = {'s':1,'r':3,'a':6,'g':2,'j':4}
# a = sorted(d.items(), key=lambda x: x[1],reverse=True)

