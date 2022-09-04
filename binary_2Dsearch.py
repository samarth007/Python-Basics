
import time


def binary_2DSearch(array,target):
    m=len(array)  #no of rows
    if m==0:
        return False
    n=len(array[0])  #no of columns
    left=0
    end= m*n-1

    while left <= end:
        mid=left+(end-left)//2
        mid_element=array[mid//n][mid%n]
        if mid_element==target:
            return True
        elif target < mid_element:
            end=mid-1
        else:
            left=mid+1

    return False

matrx=[[1,3,5,6],[10,14,19,21],[24,29,30,33],[35,40,45,50],[52,54,67,89],[99,100,104,120]]
target=120
start=time.time()
result= binary_2DSearch(matrx,target)
end=time.time()-start
print(result)
print(end)

# n=4
# m=6
# matrx=[[1,3,5,6],[10,14,19,21],[24,29,30,33],[35,40,45,50],[52,54,67,89],[99,100,104,120]]
# target=120
# start=time.time()
# for i in range(m):
#     for j in range(n):
#         if matrx[i][j]==target:
#             print('True')
# end=time.time()-start    
# print(end)