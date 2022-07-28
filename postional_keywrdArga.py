
def postionalAndKeyword(*a,**b):
    print(a)              #Positional argument should be placed before Keyword argument
    print(b)              # return type of keyword arg is dictonary
                          # return type of positional arg is tuple

postionalAndKeyword('Hi','Hello',age=27,role='ML')#Here "Hi" is positional argument and age,role are Keyword arguments



