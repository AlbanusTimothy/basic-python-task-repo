
#calculating NHIF based on gross salary
def calculate_nhif(gross_salary):
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
    return nhif


#calculating NSSF
def calculate_nssf(gross_salary):
    if gross_salary >= 18000:
        nssf = 0.06 * gross_salary
    else:
        nssf = 1080
    return nssf


#CALCULATING NHDF
def calculate_nhdf(gross_salary):
    nhdf = 0.015 * gross_salary
    return nhdf


#Calculating Taxable Income
def calculate_taxable_income(gross_salary, nssf, nhdf, nhif):
    taxable_income = gross_salary - (nssf + nhdf + nhif)
    return taxable_income


#Calculating Payee
def calculate_payee(taxable_income):
    relief = 2400  # personal relief

    if taxable_income <= 24000:
        payee = taxable_income * 0.10
    elif taxable_income <= 32333:
        payee = (24000 * 0.10) + ((taxable_income - 24000) * 0.25)
    elif taxable_income <= 500000:
        payee = (24000 * 0.10) + (8333 * 0.25) + ((taxable_income - 32333) * 0.30)
    elif taxable_income <= 800000:
        payee = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) + ((taxable_income - 500000) * 0.325)
    else:
        payee = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) + (300000 * 0.325) + ((taxable_income - 800000) * 0.35)

    #subtracting personal relief
    payee = payee - relief

    #When PAYEE is  negative
    if payee < 0:
        payee = 0

    return round(payee, 2)


# Function to calculate Net Salary
def calculate_net_salary(gross_salary, nhif, nhdf, nssf, payee):
    net_salary = gross_salary - (nhif + nhdf + nssf + payee)
    return net_salary


#user input
gross_salary = float(input("Enter Gross Salary(your salary plus benefits) (KES): "))

# Calculations
nhif_amount = calculate_nhif(gross_salary)
nssf_amount = calculate_nssf(gross_salary)
nhdf_amount = calculate_nhdf(gross_salary)
taxable_income = calculate_taxable_income(gross_salary, nssf_amount, nhdf_amount, nhif_amount)
payee_amount = calculate_payee(taxable_income)
net_salary = calculate_net_salary(gross_salary, nhif_amount, nhdf_amount, nssf_amount, payee_amount)

#   End results
print("--- Salary Breakdown ---")
print("Gross Salary:", gross_salary)
print("NHIF Deduction:", nhif_amount)
print("NSSF Deduction:", nssf_amount)
print("NHDF Deduction:", nhdf_amount)
print("Taxable Income:", taxable_income)
print("PAYEE (After Relief):", payee_amount)
print("Net Salary:", round(net_salary, 2))
