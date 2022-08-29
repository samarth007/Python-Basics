from calendar import c
from collections import Counter

val='How are you doing ? JosH'
cts=Counter(val)
print(cts.items())
# print(cts.values())
print(cts.most_common(3))