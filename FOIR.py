

def calculate_foir(income, fixed_obligations):
    return fixed_obligations / income * 100

income = float(input("Enter your monthly income: "))
fixed_obligations = float(input("Enter total monthly fixed obligations: "))

foir = calculate_foir(income, fixed_obligations)
print("Your FOIR is:", round(foir, 2), "%")
