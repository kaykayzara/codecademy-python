"""
Project: Receipts for Lovely Loveseats (Codecademy – Learn Python 3)

Concept:
- Practice Python fundamentals by generating a simple receipt.
- Skills: variables, strings, floats, string concatenation, +=, basic arithmetic,
  order of operations, and printing formatted output.

Notes:
- Prices are floats.
- `+=` is used to accumulate totals and item descriptions.
- Sales tax is applied after summing pre-tax items.
- Optional polish: use f-strings for currency: f"${total:.2f}"
"""

# -----------------------------
# TASK 1: Catalog – item 1
# Create a variable called lovely_loveseat_description that describes the Lovely Loveseat.
# -----------------------------

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend " \
"on wood. 32 inch high x 40 inch wide x 40inch deep."

# -----------------------------
# TASK 2: Catalog – item 1 price
# Set the price for the Lovely Loveseat to 254.00.
# -----------------------------

lovely_loveset_price = 254.00

# -----------------------------
# TASK 3: Catalog – item 2
# Create text that describes the Stylish Settee.
# -----------------------------

stylish_settee_description = "Stylish Settee. Fauz leather on birch. 29.5 inch " \
"high x 54.75 inch wide x 28 inch deep. Black."

# -----------------------------
# TASK 4: Catalog – item 2 price
# Set the price for the Stylish Settee to 180.50.
# -----------------------------

stylish_settee_price = 180.50

# -----------------------------
# TASK 5: Catalog – item 3
# Create text that describes the Luxurious Lamp.
# -----------------------------

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inch tall. Brown" \
"with cream shade."

# -----------------------------
# TASK 6: Catalog – item 3 price
# Set the price for the Luxurious Lamp to 52.15.
# -----------------------------

luxurious_lamp_price = 52.15

# -----------------------------
# TASK 7: Sales tax
# Define sales_tax as 0.088 (8.8%).
# -----------------------------

sales_tax = 0.088

# -----------------------------
# TASK 8: Customer running total (pre-tax)
# Initialize customer_one_total = 0.
# -----------------------------

customer_one_total = 0

# -----------------------------
# TASK 9: Customer itemization text
# Initialize customer_one_itemization = "" (empty string to append item names).
# -----------------------------

customer_one_itemization = ""

# -----------------------------
# TASK 10: Purchase 1 – add price
# Add Lovely Loveseat price to customer_one_total using +=.
# -----------------------------

customer_one_total += lovely_loveset_price

# -----------------------------
# TASK 11: Purchase 1 – record description
# Append Lovely Loveseat description to customer_one_itemization (e.g., add a newline).
# -----------------------------

customer_one_itemization += luxurious_lamp_description

# -----------------------------
# TASK 12: Purchase 2 – add price
# Add Luxurious Lamp price to customer_one_total using +=.
# -----------------------------

customer_one_total += luxurious_lamp_price

# -----------------------------
# TASK 13: Purchase 2 – record description
# Append Luxurious Lamp description to customer_one_itemization.
# -----------------------------

customer_one_itemization += luxurious_lamp_description

# -----------------------------
# TASK 14: Compute tax on current subtotal
# customer_one_tax = customer_one_total * sales_tax
# -----------------------------

customer_one_tax = customer_one_total * sales_tax

# -----------------------------
# TASK 15: Add tax to total (final amount)
# customer_one_total = customer_one_total + customer_one_tax
# -----------------------------

customer_one_total += customer_one_tax

# -----------------------------
# TASK 16: Print receipt header for items
# print("Customer One Items:")
# -----------------------------

print("Customer One Items:")

# -----------------------------
# TASK 17: Print itemization (the list of items purchased)
# print(customer_one_itemization)
# -----------------------------

print(customer_one_itemization)

# -----------------------------
# TASK 18: Print receipt header for total
# print("Customer One Total:")
# -----------------------------

print("Customer One Total:")

# -----------------------------
# TASK 19: Print final total (optionally formatted to 2 decimals)
# print(customer_one_total)            # or: print(f"${customer_one_total:.2f}")
# -----------------------------

print(customer_one_total)

# -----------------------------
# TASK 20: End
# Receipt is complete: catalog built, purchases recorded, tax applied, totals printed.
# -----------------------------
