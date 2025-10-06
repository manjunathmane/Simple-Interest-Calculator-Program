P=int(input("Enter the principal:"))
R=int(input("Enter the Rate of interest:"))
T=int(input("Enter the time:"))
SI=(P*R*T)/100
print("Simple interest is: ",{SI})
amount = P*(1+R/100)**T
CI = amount - P
print("Compound interest is: ",{CI})
