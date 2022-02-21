num=25
Allowed_num_guess=3
number_of_gues=1
print("Number of guess is limited to : ",Allowed_num_guess)
while(number_of_gues<=Allowed_num_guess):
    user_input=int(input("enter the number"))
    if user_input<num:
        print("You entered smaller number. Please enter greater number")
    elif user_input>num:
        print("You entered greater number. Please enter smaller number")
    else:
        print("You Won !!!!")
        break
    print("Number of guess left : ",Allowed_num_guess-number_of_gues)
    number_of_gues=number_of_gues+1
if number_of_gues>Allowed_num_guess:
    print("You Fail.GAME OVER !!!!")