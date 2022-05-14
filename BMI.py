
def bmi():
  Ht =float(input("enter height in m"))
  if Ht>2:
      print("enter valid height")
      return 0
  Wt = float(input("enter weight in kg"))
  if Wt>=150:
      print("enter valid weight")
      return 0
  b=Wt/(Ht**2)
  print('BMI : ',b)

  if b<=18.5:
      print('Under')
  elif b>18.5 and b<=24.9:
      print('Normal Weight')
  elif b>=25 and b<=29.9:
      print('OverWeight')
  elif b>=30 and b<=35:
      print('Obesity')
  else:
      print('Severe')

  bmi()
bmi()
