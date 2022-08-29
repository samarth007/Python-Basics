
def bubble_sort(elements):
    size=len(elements)-1

    for j in range(size):
      swapped=False
      for i in range(size-j):
         if elements[i] > elements[i+1]:
            temp=elements[i]
            elements[i]=elements[i+1]
            elements[i+1]=temp
            swapped=True
      if not swapped:
          break
    print(elements)

num_list=[2,3,6,9,12,20]
# num_list=[23,42,1,12,22,45,12,7,2]
bubble_sort(num_list)
