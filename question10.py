
# stock calculator
# Given list of products
prods = [
    ['omo', '30kshs', '300'],
    ['milk', '50kshs', '200'],
    ['bread', '45kshs', '359'],
    ['coffee', '5kshs', '79']
]

# Compute total stock using list comprehension
total_stock = sum(int(item[-1]) for item in prods)

# Display the result
print("Total stock in the company is:", total_stock)
