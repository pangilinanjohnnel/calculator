charge_per_kwh = 12.6435 #meralco standard 2025

#loop for repeatability
while True:
    item = input("Enter your item: (press q to quit):").lower()
    if item == "q":
        break
    #try except for checking non numerical value and if for zero or negative value
    try:
        watts = float(input("Enter energy in watts: "))
        if watts <= 0:
            print("Energy cannot be zero or negative")
            exit()
    except ValueError:
        print("Error, please enter numeric input")
        exit()
    try:
        hours = float(input("Enter usage time in hours: "))
        if hours <= 0:
            print("Hours cannot be zero or negative")
            exit()
    except ValueError:
        print("Error, please enter numeric input")
        exit()

    #conversion kWh
    kilowatts = watts/1000
    kWh = kilowatts * hours

    #bil calculation
    bill = kWh*charge_per_kwh
    print(f"your {item} energy consumption is {kWh:.3f} kWh")
    print(f"your current bill is: ₱{bill:.2f}")

