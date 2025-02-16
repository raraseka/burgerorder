print("Welcome to Burger Shop!")
size = input("What size burger do you want? M, N, or L:")
add_mushroom = input("Do you want to add mushroom? Y or N:")
add_extra_cheese = input("Do you want to add extra cheese? Y or N:")
bill = 0 #ask bill we need to calculate?
if size == "M":
    bill += 5
elif size == "N":
    bill += 8
else:
    bill += 10
if add_mushroom == "Y":
    if size == "L":
        bill += 2
    else:
        bill += 1
if add_extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")
    

