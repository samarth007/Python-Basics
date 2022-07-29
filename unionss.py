odd={1,3,5,7,9,2}
even={0,2,4,6,8}
primes={2,3,5,7}
un=odd.union(even)  #comines both, duplicates are removed off
inter=odd.intersection(primes)
print(inter)

ss="Hello World"
substr=ss[:7:2]
print(substr)

a="Hello How are you"
print(a.split())
print(a.split('are'))