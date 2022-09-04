

def print_formatted(number):
    # your code goes here
     bin_len = len(bin(number))-2
     print(bin_len)
     for n in range(1,number+1):
        octal = format(n, 'o')
        hexa = format(n, 'X')
        binary = format(n, 'b')
        print(f'{str(n).rjust(bin_len)} {octal.rjust(bin_len)} {hexa.rjust(bin_len)} {binary.rjust(bin_len)}')

print_formatted(5)        

print(str(5).rjust(3))
print("hi")




print('----------------------------------------------------------')


xx=2

for i in range(1,xx+1):
  octal=format(i,'o')
  hexad=format(i,'X')
  binry=format(i,'b')
  print(octal,hexad,binry)

print('This is {0:.2f}%'.format(100.125353))

print('The {} of 100 is {:b}'.format(100,100))  #printing binary
print(format(255,'x'))       #printing hexadecimal

