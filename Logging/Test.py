import logging as lg
import os

lg.basicConfig(filename='Test_log.log', level=lg.INFO)
def add_sum(*args):
    sum=0
    for i in args:
        lg.info("user entered :",str(i))
        sum=sum+i
        lg.info("Sum Value is :",str(sum))
add_sum(1,3,6,31,6)

# f=open(os.getcwd()+'/'+'Test_log.log','r')
# print(f.read())

