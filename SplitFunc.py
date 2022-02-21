
word='geeks for geeks'
text='geeks,for,geeks'
test='catratsatmata'
print(word.split())
print(text.split())
print(text.split(','))
print(test.split('t'))
print('-------------------------------------')

def rec(n):
    c=1
    d=1
    if n==1:
        return n
    else:
        while c<=n:
          d = d*c
          c=c+1
        return d
print(rec(5))

print('-------------------------------------')

#recursive factorial
def recursive(d):
    if d==1:
        return d
    else:
        d=d* recursive(d-1)
    return d
print(recursive(5))