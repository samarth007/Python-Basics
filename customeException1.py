
class SalaryNotInRange(Exception):
    def __init__(self,message):
        super().__init__(message)

salary=int(input('Enter Salary :').strip())

try:
    if not 5000<salary<10000:
        raise SalaryNotInRange("Salary not in range")
    
except SalaryNotInRange as s:
    print(s)                         # Handle the execption

else:
    print("Entered Correct Salary")   #This block will only execute if there is no exception in try block

finally:
    print("Terminating")           # Always executes
