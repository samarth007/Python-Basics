# class dobException(Exception):
#     pass
#
# year= int(input("Enter the DOB : "))
# age=2021-year
# try:
#     if age<=30 & age>20:
#         print('valid')
#     else:
#         raise dobException
# except dobException:
#     print('Invalid')

ll=[]
def sqre(l):
    ll=[i**2 for i in l if i%2==0]
    return ll

print(sqre([1,2,3,4]))