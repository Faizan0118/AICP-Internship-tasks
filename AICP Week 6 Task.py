#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Constants for weight limits
MIN_WEIGHT_CEMENT = 24.9
MAX_WEIGHT_CEMENT = 25.1
MIN_WEIGHT_SAND_GRAVEL = 49.9
MAX_WEIGHT_SAND_GRAVEL = 50.1

# Prices
PRICE_CEMENT = 3
PRICE_SAND = 2
PRICE_GRAVEL = 2
PRICE_SPECIAL_PACK = 10

def validate_sack(contents, weight):
    """
    Validates a single sack based on its contents and weight.
    Returns a tuple (valid, rejection_reason).
    """
    if contents not in ['C', 'G', 'S']:
        return False, "Invalid contents. Must be C (cement), G (gravel), or S (sand)."

    if contents == 'C' and not (MIN_WEIGHT_CEMENT < weight < MAX_WEIGHT_CEMENT):
        return False, "Invalid weight for cement sack."

    if contents in ['G', 'S'] and not (MIN_WEIGHT_SAND_GRAVEL < weight < MAX_WEIGHT_SAND_GRAVEL):
        return False, "Invalid weight for sand or gravel sack."

    return True, None

def calculate_regular_price(num_cement, num_gravel, num_sand):
    """
    Calculate and output the regular price for a customer's order.
    """
    regular_price = (num_cement * PRICE_CEMENT) + (num_gravel * PRICE_GRAVEL) + (num_sand * PRICE_SAND)
    print(f"Regular price for the order: ${regular_price}")
    return regular_price

def calculate_discount_price(num_cement, num_gravel, num_sand):
    """
    Calculate and output the discount price for a special pack.
    """
    num_special_packs = min(num_cement, num_gravel // 2, num_sand // 2)
    discount_price = num_special_packs * PRICE_SPECIAL_PACK

    if num_special_packs > 0:
        print(f"Discount price for special packs: ${discount_price}")
    return discount_price

def process_customer_order():
    """
    Process input for a customer's order, check each sack, and output the results.
    """
    total_weight = 0
    sacks_rejected = 0

    num_cement_required = int(input("Enter the number of cement sacks required: "))
    num_gravel_required = int(input("Enter the number of gravel sacks required: "))
    num_sand_required = int(input("Enter the number of sand sacks required: "))

    num_cement_received = 0
    num_gravel_received = 0
    num_sand_received = 0

    for _ in range(num_cement_required):
        contents = 'C'
        weight = float(input("Enter weight of the cement sack in kilograms: "))
        valid, rejection_reason = validate_sack(contents, weight)

        if valid:
            total_weight += weight
            num_cement_received += 1
        else:
            sacks_rejected += 1
            print(f"Sack rejected. Reason: {rejection_reason}")

    for _ in range(num_gravel_required):
        contents = 'G'
        weight = float(input("Enter weight of the gravel sack in kilograms: "))
        valid, rejection_reason = validate_sack(contents, weight)

        if valid:
            total_weight += weight
            num_gravel_received += 1
        else:
            sacks_rejected += 1
            print(f"Sack rejected. Reason: {rejection_reason}")

    for _ in range(num_sand_required):
        contents = 'S'
        weight = float(input("Enter weight of the sand sack in kilograms: "))
        valid, rejection_reason = validate_sack(contents, weight)

        if valid:
            total_weight += weight
            num_sand_received += 1
        else:
            sacks_rejected += 1
            print(f"Sack rejected. Reason: {rejection_reason}")

    print(f"\nTotal weight of the order: {total_weight} kg")
    print(f"Number of sacks rejected: {sacks_rejected}")
    print(f"Number of cement sacks received: {num_cement_received}")
    print(f"Number of gravel sacks received: {num_gravel_received}")
    print(f"Number of sand sacks received: {num_sand_received}")

    return num_cement_received, num_gravel_received, num_sand_received

# Test the program
print("=== Process a customer order ===")
num_cement, num_gravel, num_sand = process_customer_order()

# Calculate regular and discount prices
regular_price = calculate_regular_price(num_cement, num_gravel, num_sand)
discount_price = calculate_discount_price(num_cement, num_gravel, num_sand)

# Calculate and output the new price for the order and the amount saved
new_price = regular_price - discount_price if discount_price > 0 else regular_price
amount_saved = regular_price - new_price if discount_price > 0 else 0

print(f"\nNew price for the order: ${new_price}")
print(f"Amount saved: ${amount_saved}")


# In[ ]:




