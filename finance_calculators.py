import math
#Financial calculator

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

print("Enter either 'investment'or 'bond' from the menu above to proceed:")
# decision is used to represent what the user chooses
decision = input()
#if user chooses investment

if decision == "investment" or decision == "Investment" or decision == "INVESTMENT":
    P = float(input("Enter deposit amount:"))
    R = float(input("Enter interest rate as a number:"))
    r = float(R/100) #interest rate is in percentage

    t = int(input("Enter total years for investment:"))

    interest = input("Enter type of interest:\ncompound\nsimple\n")
    if interest == "simple":
        A = P * (1 + r*t)
    elif interest == "compound":
        A = P * math.pow((1+r),t)
    else:
        print("Invalid Selection")
    print("Your new amount after", t, "years is", round(A,2))

#if user chooses bond

if decision == "bond" or "Bond" or "BOND":
    P = float(input("Enter the present value of the house:"))
    R = float(input("Enter the interest rate:"))
    r = float(R/100) #interest rate is in percentage
    
    n = int(input("Enter number of months for repayment:"))
    i = r/12

    repayment = (i * P)/(1 - (1 + i)**(-n))
    print("The repayment amount after", n, "months is", round(repayment,2))

else:
    print("Invalid Selection")