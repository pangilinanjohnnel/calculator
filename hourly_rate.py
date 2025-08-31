try:
    hours = float(input("Enter hours: "))
    hourly_rate = float(input("Enter Hourly Rate: "))
except ValueError:
    print("Error, please enter numeric input")
    exit()

if hours > 40:
    regular_pay = 40 * hourly_rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours * hourly_rate

print(f"your total gross pay is:P {gross_pay:.2f}")

tax=gross_pay * 0.15
net_pay=gross_pay-tax

print (f"your total net_pay is: P {net_pay:.2f}")