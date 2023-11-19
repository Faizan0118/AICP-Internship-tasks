#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Source data (two-dimensional array)
electricity_matrix = [
    [55, 65, 75],   # Slab 1
    [120, 150, 170], # Slab 2
    [210, 230, 240]  # Slab 3
]

# Function to calculate and display cost for slab 1
def costSlab1():
    print("Bill for slab 1 is:")
    #print("Unit Range: 0 to 100")
    #print("Cost per unit: Rs.10")
    print("Total Cost:", end=" ")
    for value in electricity_matrix[0]:
        cost = value * 10
        print(cost, end="   ")
    print()  # Move to the next line

# Function to calculate and display cost for slab 2
def costSlab2():
    print("Bill for slab 2 is:")
    #print("Unit Range: 101 to 200")
    #print("Cost per unit: Rs.15")
    print("Total Cost:", end=" ")
    for value in electricity_matrix[1]:
        cost = value * 15
        print(cost, end="   ")
    print()  # Move to the next line

# Function to calculate and display cost for slab 3
def costSlab3():
    print("Bill for slab 3 is:")
    #print("Unit Range: 201 to 300")
    #print("Cost per unit: Rs.20")
    print("Total Cost:", end=" ")
    for value in electricity_matrix[2]:
        cost = value * 20
        print(cost, end="   ")
    print()  # Move to the next line

# Display student's ID at the top of the menu
student_id = "23Y620008"
print("Student ID:", student_id)

# Repeating menu
while True:
    print("\nEnter Your Choice:")
    print("Press 1 to display the bill of slab 1 and slab 2")
    print("Press 2 to display the bill of slab 3")
    print("Press any other key to exit")
    
    choice = input("Enter your choice (1, 2, or any other key to exit): ")

    if choice == '1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    elif choice != '1' and choice !='2':
        print("Program Terminated!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or exit.")


# In[ ]:





# In[ ]:




