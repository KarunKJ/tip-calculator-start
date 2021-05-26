#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print('Welcome to the Tip calculator')
Total_amt = input("Enter total bill amount?")
Tip_percentage = input("Enter what percentage tip would ypu like to give? 10, 12 or 15?")
new_tip = float(Tip_percentage)
new_total = float(Total_amt)
new_total_incl_tip = new_total*(1 + (new_tip/100))
people = float(input("How many ppl to split?"))
total_pp = round(new_total_incl_tip/people, 2)
print(f"Each person should pay ${total_pp}")