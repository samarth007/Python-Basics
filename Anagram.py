
def m(s1,s2):

 if(len(s1)!=len(s2)):
   #print("Non Anagram")
   return 0

 s1 =sorted(s1.lower())
 s2 =sorted(s2.lower())

 for i in range(len(s1)):
     if(ascii(s1[i])!=ascii(s2[i])):
         return 0


if type(m('race', 'Care'))== int:
    print("non Anagram")
else:
    print("Anagram")


