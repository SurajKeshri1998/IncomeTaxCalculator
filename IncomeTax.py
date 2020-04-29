income=float(input("Enter Your Income: "))
tax=0
cess=0

if income<=250000:
    tax=0
elif income<=500000:
    tax=(income-250000)*0.05
elif income<=1000000:
    tax=12500+(income-500000)*0.2
else:
    tax=12500+100000(income-1000000)*0.3

cess=tax*0.04
Total_Tax=tax+cess

print("Income Tax: ",tax)
print("Health and Education: ",cess)
print("Total Tax: ",Total_Tax)
print(f"Your Income is {income} and Total Tax is {Total_Tax}")