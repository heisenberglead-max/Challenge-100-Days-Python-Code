# Input accepts data as string so we need to specify what type we are giving.
print("Welcome to the tip calculator.")
total_amount=float(input("How much is the total bill? $"))
tip_percent=int(input("What percentage of tip you wanna give to 10, 12, 15?"))
total_bill=total_amount+total_amount*(tip_percent/100)
no_of_people=int(input("Among how many you wanna split the bill?"))
to_pay=total_bill/no_of_people
print("Each person have to pay is :"+str(round(to_pay,2)))  
