#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Constants
COST_PER_HOUR = 20
COST_PER_HALF_HOUR = 12
OPENING_TIME = 10
CLOSING_TIME = 17

# Variables
money_taken = 0
total_hours_hired = 0
boat_schedule = {boat_number: {'end_time': OPENING_TIME, 'hours_hired': 0} for boat_number in range(1, 11)}

# Function to calculate cost based on time
def calculate_cost(hours):
    if hours >= 1:
        return COST_PER_HOUR * hours
    else:
        return COST_PER_HALF_HOUR * (hours * 2)

# Function to find the next available boat
def find_next_available_boat(current_time):
    available_boats = [boat_number for boat_number, schedule in boat_schedule.items() if schedule['end_time'] <= current_time]
    if available_boats:
        return min(available_boats, key=lambda x: boat_schedule[x]['end_time'])
    else:
        return None

# Input for each boat
for boat_number in range(1, 11):
    print(f"\nBoat {boat_number}:")

    # Input start time
    start_time = int(input("Enter start time (between 10 and 17): "))
    
    # Validate start time
    if start_time < OPENING_TIME or start_time >= CLOSING_TIME:
        print("Error: Boat can't be hired before 10:00 or after 17:00.")
        continue
    
    # Find the next available boat
    next_available_boat = find_next_available_boat(start_time)
    
    # If no boats are available, show the earliest time
    if next_available_boat is None:
        earliest_available_time = min(boat_schedule.values(), key=lambda x: x['end_time'])['end_time']
        print(f"No boats available. The earliest available time is: {earliest_available_time}")
        break
    
    # Input end time
    end_time = int(input("Enter end time (between start time and 17): "))
    
    # Validate end time
    if end_time <= start_time or end_time > CLOSING_TIME:
        print("Error: Invalid end time.")
        continue
    
    # Calculate hours hired
    hours_hired = end_time - start_time
    
    # Calculate cost
    boat_cost = calculate_cost(hours_hired)
    
    # Update total hours and money taken
    total_hours_hired += hours_hired
    money_taken += boat_cost
    
    # Update boat schedule
    boat_schedule[boat_number]['end_time'] = end_time
    boat_schedule[boat_number]['hours_hired'] += hours_hired
    
    # Output boat details
    print(f"Boat {boat_number} hired for {hours_hired} hours. Cost: ${boat_cost}")

# Output total money taken and hours hired
print("\nTotal money taken for the day: ${}".format(money_taken))
print("Total hours hired for the day: {}".format(total_hours_hired))

# Calculate boats not used and boat used the most
boats_not_used = [boat_number for boat_number, schedule in boat_schedule.items() if schedule['hours_hired'] == 0]
boat_used_the_most = max(boat_schedule, key=lambda x: boat_schedule[x]['hours_hired'])

# Output report
print("\nBoats not used today: {}".format(boats_not_used))
print("Boat used the most today: {} ({} hours)".format(boat_used_the_most, boat_schedule[boat_used_the_most]['hours_hired']))


# In[ ]:




