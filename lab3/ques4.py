def simple_interest(principal, rate, time):
    SI = (principal * rate * time) / 100
    return SI

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

# Calculate and display simple interest
SI = simple_interest(principal, rate, time)
print(f"The Simple Interest is: {SI}")
