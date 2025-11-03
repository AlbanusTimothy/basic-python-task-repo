# ---------------------------------------------------------------------------------------QUESTION 15--------------------------------------
# calculating nhif
# Get user input
basic_salary = float(input("Enter Basic Salary (KES): "))
benefits = float(input("Enter Benefits (KES): "))

# Calculate gross salary
gross_salary = basic_salary + benefits

# Calculate NHIF directly (no function)
if gross_salary <= 5999:
    nhif = 150
elif gross_salary <= 7999:
    nhif = 300
elif gross_salary <= 11999:
    nhif = 400
elif gross_salary <= 14999:
    nhif = 500
elif gross_salary <= 19999:
    nhif = 600
elif gross_salary <= 24999:
    nhif = 750
elif gross_salary <= 29999:
    nhif = 850
elif gross_salary <= 34999:
    nhif = 900
elif gross_salary <= 39999:
    nhif = 950
elif gross_salary <= 44999:
    nhif = 1000
elif gross_salary <= 49999:
    nhif = 1100
elif gross_salary <= 59999:
    nhif = 1200
elif gross_salary <= 69999:
    nhif = 1300
elif gross_salary <= 79999:
    nhif = 1400
elif gross_salary <= 89999:
    nhif = 1500
elif gross_salary <= 99999:
    nhif = 1600
else:
    nhif = 1700


# -------------------------------------------------------------------------------------------END OF QUESTION 15-----------------------------------------------
# --------------------------------------------------------------------------------------------QUESTION 16---------------------------------------------------
# Calculating NSSF 
if gross_salary >= 18000:
    nssf = gross_salary * 0.06
else:
    nssf =0  
# --------------------------------------------------------------------------------------QUESTION 17----------------------------------------------------
# Calculating NHDF
# --- NHDF Calculation ---
nhdf = gross_salary * 0.015

#--------------------------------------------------------------------------------------END OF QUESTION 17------------------------------------------------
# -----------------------------------------------------------------------------------QUESTION 18-------------------------------------------------------------
# Calculating taxable income
taxable_income=gross_salary-(nhif+nssf+nhdf)
# ---------------------------------------------------------------------------------------END OF QUESTION 18------------------------------------------------
# -------------------------------------------------------------------------------------------QUESTION 19---------------------------------------------------
# Calculating PAYEE
# Personal relief
personal_relief = 2400

# PAYE calculation
if taxable_income <= 24000:
    payee = taxable_income * 0.1
elif taxable_income <= 32333:
    payee = 24000 * 0.1 + (taxable_income - 24000) * 0.25
elif taxable_income <= 500000:
    payee = 24000 * 0.1 + 8333 * 0.25 + (taxable_income - 32333) * 0.3
elif taxable_income <= 800000:
    payee = 24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 + (taxable_income - 500000) * 0.325
else:
    payee = 24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 + 300000 * 0.325 + (taxable_income - 800000) * 0.35

# Deduct personal relief
payee -= personal_relief

# Prevent negative PAYE
if payee < 0:
    payee = 0
# ----------------------------------------------------------------------------------------------------------------------END OF QUESTION 19----------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------QUESTION 20-------------------------------------------
# Calculating net income
net_income= gross_salary-(nhif+nssf+nhdf+payee)
# Display results
print("--- SALARY DETAILS ---")
print("Gross Salary:", gross_salary)
print("NHIF Deduction:", nhif)
print("NSSF Deduction:", nssf)
print("NHDF Deduction:", nhdf)
print("Taxable Income:",taxable_income)
print("PAYEE (KES):", round(payee, 2))
print("Your net income is:",net_income)
