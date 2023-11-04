#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Define constants for component categories
CASE = "Case"
RAM = "RAM"
MAIN_HDD = "Main Hard Disk Drive"
SSD = "Solid State Drive"
SECOND_HDD = "Second Hard Disk Drive"
OPTICAL_DRIVE = "Optical Drive"
OS = "Operating System"

# Define arrays to store the item data
items = [
    (CASE, "A1", "compact", 75.00),
    (CASE, "A2", "tower", 150.00),
    (RAM, "B1", "8gb", 79.99),
    (RAM, "B2", "16gb", 149.99),
    (RAM, "B3", "32gb", 299.99),
    (MAIN_HDD, "C1", "1TB HDD", 49.99),
    (MAIN_HDD, "C2", "2TB HDD", 89.99),
    (MAIN_HDD, "C3", "4TB HDD", 129.99),
    (SSD, "D1", "240Gb SSD", 59.99),
    (SSD, "D2", "480Gb SSD", 119.99),
    (SECOND_HDD, "E1", "1TB HDD", 49.99),
    (SECOND_HDD, "E2", "2TB HDD", 89.99),
    (SECOND_HDD, "E3", "4TB HDD", 129.99),
    (OPTICAL_DRIVE, "F1", "DVD/Blu-Ray Player", 50.00),
    (OPTICAL_DRIVE, "F2", "DVD/Blu-Ray Re-writer", 100.00),
    (OS, "G1", "Standard Version", 100.00),
    (OS, "G2", "Professional Version", 175.00),
]

# Initialize variables to store the selected components and total price
selected_components = {CASE: None, RAM: None, MAIN_HDD: None}
basic_components_cost = 200.00
total_price = basic_components_cost  # Total price of components, including basic cost
additional_items = []  # Store the selected additional items

# Function to display the list of available items in a category
def display_items(category):
    print(f"Available {category} options:")
    for item in items:
        if item[0] == category:
            print(f"Item code {item[1]} - {item[2]}, Price: ${item[3]:.2f}")

# Function to select an item from a category
def select_item(category):
    display_items(category)
    while True:
        item_code = input(f"Enter the item code for {category}: ").strip()
        for item in items:
            if item[0] == category and item[1] == item_code:
                selected_components[category] = item
                return item

# Select one case, one RAM, and one Main Hard Disk Drive
select_item(CASE)
select_item(RAM)
select_item(MAIN_HDD)

# Calculate the initial price of the computer
for component in selected_components.values():
    total_price += component[3]
   # Function to add additional items and update the total price
def add_additional_items():
    global total_price  # Make total_price a global variable
    while True:
        choice = input("Do you want to purchase additional items? (yes/no): ").strip().lower()
        if choice == "no":
            break
        elif choice == "yes":
            print("Additional item codes:")
            for item in items:
                if item[0] not in (CASE, RAM, MAIN_HDD):
                    print(f"Item code {item[1]} - {item[2]}, Price: ${item[3]:.2f}")
            item_code = input("Enter the item code for the additional item: ").strip()
            for item in items:
                if item[1] == item_code:
                    additional_items.append(item)
                    total_price += item[3]
                    print(f"Added {item[2]} to the computer. New total price: ${total_price:.2f}")
                    break
            else:
                print("Invalid item code. Please try again.")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Add additional items and update the total price
add_additional_items()

# Display the selected components and final price
print("Selected components:")
for category, item in selected_components.items():
    print(f"{category}: {item[2]} - ${item[3]:.2f}")

# Calculate the initial total price
total_price += basic_components_cost

# Calculate the number of additional items
num_additional_items = len(additional_items)

# Apply discounts based on the number of additional items
discount = 0
if num_additional_items == 1:
    discount = total_price * 0.05
elif num_additional_items >= 2:
    discount = total_price * 0.10

# Display the final price and apply discounts
if num_additional_items > 0:
    print(f"Total price before discount: ${total_price - basic_components_cost:.2f}")
    print(f"Discount: ${discount:.2f}")
    total_price -= discount
    print(f"Total price after discount: ${total_price - basic_components_cost:.2f}")
else:
    print(f"Total price: ${total_price - basic_components_cost:.2f}")


# In[ ]:





# In[ ]:




