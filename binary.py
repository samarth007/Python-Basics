
#Binary search works only on sorted list

def binary_search(number_list,number_find):
    left_index=0
    right_index=len(number_list)-1

    while left_index <= right_index:
      mid_index=(left_index+right_index)//2
      if number_list[mid_index] == number_find:
        return mid_index

      if number_list[mid_index] < number_find:
        left_index=mid_index+1
      else:
        right_index=mid_index-1

    return -1

num_list=[12,23,37,39,45,56,59,74,84,99,100]
num_find=101
index=binary_search(num_list,num_find)
print("Index of {0} is {1}".format(num_find,index))






