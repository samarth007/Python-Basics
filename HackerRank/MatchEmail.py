import re

def fun(s):
    pattern = re.compile(r"^([a-zA-Z0-9\-_]+)\@([a-zA-Z0-9]+)\.([a-zA-Z]{,3})$")
    pattern=re.compile(r"^([a-zA-Z0-9\-_]+)\@([a-zA-Z0-9]+)\.([a-zA-Z]{,3})$")
    x = bool(pattern.match(s))
    y=pattern.match(s)
    print(x)
    if x:
        return True
    else:
        return False


fun('samarthakrao@gmail.com')
