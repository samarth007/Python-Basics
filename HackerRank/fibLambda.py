cube = lambda x:x**3 

def fibonacci(n):
    # return a list of fibonacci numbers
    n1,n2=0,1
    arr=[]
    n3=0
    if n<0:
        return -1
    
    while n3<n:
        arr.append(n1)
        n4=n1+n2
        n1=n2
        n2=n4
        n3+=1
    return arr    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))