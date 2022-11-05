

def smart_div(func):

    def inner(x,y):
        if y==0:
            print('Division not possible !!')
        else:
            return func(x,y)
    return inner            

@smart_div
def divide(a,b):
    return a/b

print(divide(2,4))   