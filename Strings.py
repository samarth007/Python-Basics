Str='harr marr'

for i in range(0,len(Str)):
    count =1
    for j in range(i+1,len(Str)):
        if(Str[i]==Str[j] and Str[i]!=''):
            count=count+1
            Str=Str[:j]+'0'+ Str[j+1:]
    if count >1 and Str[i]!='0':
        print(Str[i])

print('-----------------------------------------')

def sub(string,substr):
    if (string.find(substr)==-1):
        print('Not Found')
    else:
        print("Found")

sub('geeks for geeks','fo')