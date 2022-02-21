import json

dir = '{"1":"one","2":"two"}'
print(dir)
print(type(dir))

par=json.loads(dir)
print(par)
print(type(par))
print('Converting string to dict')
print('--------------------------------------------')
data2={"channel":"youtube","cars":["BMW","Audi8"],"book":("science","maths")}
print(data2)
print(type(data2))

jscomp=json.dumps(data2)
print(jscomp)
print(type(jscomp))