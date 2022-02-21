
def sort_elements(elements):
   l=len(elements)-1
   for i in range(l):
      min_index=i
      for j in range(min_index+1,l):
          if elements[j] < elements[i]:
              min_index=j
               


elements=[2,43,24,72,13,35,65,14,89]
sort_elements(elements)
print(elements)