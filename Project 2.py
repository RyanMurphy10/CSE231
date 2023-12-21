import math

Banner = "\nWelcome to Horizons car rentals. \n\nAt the prompts, please enter the following: \n\tCustomer's classification code (a character: BD, D, W) \n\tNumber of days the vehicle was rented (int)\n\tOdometer reading at the start of the rental period (int)\n\tOdometer reading at the end of the rental period (int)"

print(Banner)

Prompt = "\nWould you like to continue (A/B)? "

in_str = input (Prompt)

while in_str == "A":
  code = input("\nCustomer code (BD, D, W): ")
  while code != "BD" and code != "D" and code != "W":
    print("\n	*** Invalid customer code. Try again. ***")
    code = input("\nCustomer code (BD, D, W): ")
  days = input("\nNumber of days: ")
  od_start = input("Odometer reading at the start: ")
  od_end = input("Odometer reading at the end:   ")
  miles = (float(od_end) - float(od_start))/10
  amount = 0

  if code == "BD":
    amount = 40 + 0.25 * miles
    print("\nCustomer summary:")
    print("\tclassification code: " + code)
    print("\trental period (days): " + days)
    print("\todometer reading at start: "+ str(int(od_start)))
    print("\todometer reading at end:   " + str(int(od_end)))
    print("\tnumber of miles driven:  " + str(miles))
    print("\tamount due: $ "+str(float(amount)))
  elif code == "D":
    amount = float(days) * 60 
    daily = miles / float(days)
    if daily > 100:
      amount = amount + (daily - 100) * 0.25 * float(days)
    print("\nCustomer summary:")
    print("\tclassification code: " + code)
    print("\trental period (days): " + days)
    print("\todometer reading at start: "+ str(int(od_start)))
    print("\todometer reading at end:   " + str(int(od_end)))
    print("\tnumber of miles driven:  " + str(miles))
    print("\tamount due: $ "+str(float(amount)))
  elif code == "W":
    weeks = math.ceil (float(days) / 7)
    amount = weeks * 190
    weekly = miles / weeks
    if weekly > 900 and weekly <= 1500:
      amount = amount + 100 * weeks
    elif weekly > 1500:
      amount = amount + 200 * weeks
      amount = amount + (weekly - 1500) * 0.25 * weeks
    print("\nCustomer summary:")
    print("\tclassification code: " + code)
    print("\trental period (days): " + days)
    print("\todometer reading at start: "+ str(int(od_start)))
    print("\todometer reading at end:   " + str(int(od_end)))
    print("\tnumber of miles driven:  " + str(miles))
    print("\tamount due: $ "+str(float(amount)))
  else:
    print("\t*** Invalid customer code. Try again. ***")

  in_str = input (Prompt)
print("Thank you for your loyalty.")