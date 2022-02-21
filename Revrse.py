#Reverse words in string
def reverse(s):
    s=s.split(' ')
    for i in s[::-1]:
      print(i)

reverse("geek for geeks")
print('---------------------------------')

#Swapping
def swap(s):
    s=s.replace(',','hi')
    print(s)

swap('sam,dam,ram')