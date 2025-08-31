principle=0
rate=0
time=0

while principle <= 0:
    principle= float(input("enter principle:"))
    if principle <= 0:
        print("principle can't be less than or equal to zero")
while rate <= 0:
    rate= float(input("enter rate:"))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
while time <= 0:
    time= int(input("enter year:"))
    if time <= 0:
        print("year can't be less than or equal to zero")
total=principle * pow((1+rate/100),time)

print(f"the principle is {principle} pesos with the rate of {rate}% per year")
print(f"Total balance after {time} year: {total} pesos")