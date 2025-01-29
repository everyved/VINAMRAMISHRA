# Accept shopping amount from the user
amount = float(input("Enter the shopping amount: "))

# Apply discount based on amount
if amount >= 5000:
    discount = 0.20  # 20% discount for purchases >= 5000
elif amount >= 3000:
    discount = 0.15  # 15% discount for purchases >= 3000
elif amount >= 1000:
    discount = 0.10  # 10% discount for purchases >= 1000
else:
    discount = 0.05  # 5% discount for purchases < 1000

# Calculate discount amount
discount_amount = amount * discount
final_amount = amount - discount_amount

# Display results
print(f"Original Amount: ₹{amount:.2f}")
print(f"Discount Applied: {discount * 100:.0f}%")
print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
