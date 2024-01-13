print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
split = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would ypu like to give? 10,12 or 15? "))

tip_p=tip/100
total=bill+(bill*tip_p)
spl=total/split

print(f"Total split for bill of ${bill} with a tip of {tip} percent is : {spl}")