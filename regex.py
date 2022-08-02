import re


word="GeeksforGeeks: A computer science portal for geeks"
m=re.search(r"Geeks",word)
print(m)

word1="Hello my Number is 123456789 and my friend's number is 987654321"
n=re.findall("\d",word1)
nn=re.findall("\d+",word1)

word2="I went to him at 11 A.M., he \ said *** in some_language."
ww=re.compile("\w+")   # w+ for groups, w for single character
print(ww.findall(word2))
print(n)
print(nn)


