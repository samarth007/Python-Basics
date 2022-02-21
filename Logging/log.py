import logging as lg
import os
# os.mkdir("logTest") #it will make directory
print(os.getcwd()) #return current working directory
# os.chdir(os.getcwd()+"/"+"logger") #check for the directory
lg.basicConfig(filename='logs.log',level=lg.INFO,format='%(asctime)s%(message)s')
lg.error("hi")
lg.info('hi iinfo')