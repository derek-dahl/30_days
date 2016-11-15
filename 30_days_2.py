#Given parameters
meal_cost = float(input())
tip_percent = float(input())
tax_percent = float(input())
#Formula for tip and tax
tip = meal_cost * (tip_percent/100)
tax = meal_cost * (tax_percent/100)
#Adds total tax and tip, then rounds to nearest whole number. Converts to integer
total_cost = round(meal_cost + tip + tax, 0)
total_cost = int(total_cost)

print("The total meal cost is " + str(total_cost) + " dollars.")
