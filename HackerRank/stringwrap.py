
def wrap(word, display):
     seq=int(len(word)/display)
     gap=0
     a=[]
     for i in range(seq+1):
         a.append(word[gap:gap+display])
         gap+=display
     return '\n'.join(a)

print(wrap("SAMARTHAKRAO",3).strip())         
