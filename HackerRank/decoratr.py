


# def person_lister(func):
#     def inner(people):
#         # complete the function
#         return map(func, sorted(people, key=lambda x: x[2]))          
#     return inner

# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')    



def smart(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@smart
def div(a,b):
    return a/b

print(div(6,4))

