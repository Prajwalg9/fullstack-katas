#compound intrest= CP = Amount - p
#Where, Amount =P(1+(R/100))**T &
#Where,
#P=Principal Amount
#R=Rate of Intrest
#T=Time duration

print("lets Calculate Compound Intrest\n")
P=float(input("Enter Principal Amount: "))
R=float(input("Enter Rate of Intrest: "))
T=float(input("Enter Time duration in Years: "))

Amount= P*pow((1+(R/100)),T)
CP = Amount-P
print(f"Compound Intrest is {CP}\n")