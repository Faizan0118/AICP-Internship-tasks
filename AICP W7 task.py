#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize charity names and donation totals
charities = ["Charity A", "Charity B", "Charity C"]
donation_totals = [0, 0, 0]

# Function to display charities and totals
def display_totals():
    print("\nCharity Totals So Far (Descending Order):")
    sorted_charities = sorted(zip(charities, donation_totals), key=lambda x: x[1], reverse=True)
    grand_total = 0

    for charity, total in sorted_charities:
        grand_total += total
        print(f"{charity}: ${total:.2f}")

    print("\nGRAND TOTAL DONATED TO CHARITY: ${:.2f}".format(grand_total))

# Function to get valid donation choice
def get_donation_choice():
    while True:
        try:
            choice = int(input("Enter the number of your chosen charity (1, 2, or 3), or -1 to show totals: "))
            if choice == -1 or (1 <= choice <= 3):
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3, or -1 to show totals.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main program
num_customers = int(input("Enter the number of customers: "))

# Set up charities
for i in range(3):
    charities[i] = input(f"Enter the name of Charity {i + 1}: ")

for customer in range(1, num_customers + 1):
    print(f"\nCustomer {customer}:")

    while True:
        # Display charities and totals
        display_charities()
        display_totals()

        # Get user input for donation choice
        choice = get_donation_choice()

        if choice == -1:
            break  # Show totals and exit donation loop
        else:
            # Get user input for shopping bill
            bill = get_shopping_bill()

            # Calculate and display donation
            calculate_donation(choice, bill)

# Display final totals and grand total
display_totals()


# 
