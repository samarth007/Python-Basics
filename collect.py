
from collections import Counter
import re


val='How are you doing ? JosH'
pattern=re.compile(r'How')
val=re.sub(pattern,'s',val)
print(val)
cts=Counter(val)
print(cts.items())
# print(cts.values())
print(cts.most_common(3))