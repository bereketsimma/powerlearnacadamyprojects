# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if 20% or more
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price  # No discount if less than 20%

# Prompt user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Get final price using the function
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
