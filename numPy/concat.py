import numpy

# n_rows,m_rows,p_col=map(int,input().strip().split())
n_rows,m_rows=3,3
arr1=[]
arr2=[]

for i in range(n_rows):
    a=list(map(int,input().split()))
    arr1.append(a)
 
for j in range(m_rows):
    a=list(map(int,input().split()))
    arr2.append(a)
    
arrN=numpy.array(arr1)
arrM=numpy.array(arr2)
print(arrN)
print(arrM)
print(numpy.concatenate((arrN,arrM),axis=1))

