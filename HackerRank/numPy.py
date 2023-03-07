import numpy as np

N,M=map(int,input().strip().split())

matrix=[]
for i in range(N):
    a=list(map(int,input().split()))
    matrix.append(a)
    
arr=np.array(matrix)

arr_min=np.min(arr,axis=1)
arr_max=np.max(arr_min)

print(arr_min)
print(arr_max)

arr=np.asarray([[2,3,1],[4,1,4]])
print(arr.min(axis=0))


# n_rows=int(input())
# n_columns=int(input())

# matx=[]
# for i in range(n_rows):
#     a=[]
#     for j in range(n_columns):
#         a.append(int(input()))
#     matx.append(a)

# arr=np.array(matx)
# print(arr)





       