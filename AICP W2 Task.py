#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, timedelta

class MountainRailway:
    def __init__(self):
        # Constants
        self.num_coaches = 6
        self.num_trains = 4
        self.ticket_price = 25
        self.group_discount_threshold = 10
        
         # Train schedule
        self.departure_times = [datetime.strptime(f'{i + 9}:00', '%H:%M') for i in range(self.num_trains)]
        self.return_times = [self.departure_times[i] + timedelta(hours=1) for i in range(self.num_trains)]

        # Initialize data structures
        self.passengers_up = [0] * self.num_trains
        self.passengers_down = [0] * self.num_trains
        self.money_up = [0] * self.num_trains
        self.money_down = [0] * self.num_trains
        self.available_seats_up = [self.num_coaches * 80] * self.num_trains
        self.available_seats_down = [self.num_coaches * 80 + (2 if i == self.num_trains - 1 else 0) for i in range(self.num_trains)]

    def display_screen(self):
        # Display the current state of each train journey
        for i in range(self.num_trains):
            departure_time = self.departure_times[i].strftime('%H:%M')
            return_time = self.return_times[i].strftime('%H:%M')

            print(f'Train {i + 1} (Up) - Departure Time: {departure_time}, Coaches: {self.num_coaches}, Seats available: {self.available_seats_up[i]}')
            print(f'Train {i + 1} (Down) - Return Time: {return_time}, Coaches: {self.num_coaches}, Seats available: {self.available_seats_down[i]}')
            if self.available_seats_up[i] > 0:
                print(f'Train {i + 1} (Up): {self.available_seats_up[i]} seats available')
            else:
                print(f'Train {i + 1} (Up): Closed')

            if self.available_seats_down[i] > 0:
                print(f'Train {i + 1} (Down): {self.available_seats_down[i]} seats available')
            else:
                print(f'Train {i + 1} (Down): Closed')

    def purchase_tickets(self, train_num, num_tickets):
        # Check if there are enough available seats for the selected train journey
        if train_num < 1 or train_num > self.num_trains:
            print("Error: Invalid train number.")
            return

        if num_tickets <= 0:
            print("Error: Number of tickets must be greater than zero.")
            return

        # Check if there are enough available seats for both upward and downward journeys
        if train_num == self.num_trains:  # Last train has extra coaches
            available_seats_up = self.available_seats_down[train_num - 1]
            available_seats_down = self.available_seats_down[train_num - 1]
        else:
            available_seats_up = self.available_seats_up[train_num - 1]
            available_seats_down = self.available_seats_down[train_num - 1]

        if num_tickets <= min(available_seats_up, available_seats_down):
            # Calculate total price
            total_price = num_tickets * self.ticket_price
            group_discount = (num_tickets // self.group_discount_threshold) * self.ticket_price
            total_price -= group_discount

            # Update data structures
            self.passengers_up[train_num - 1] += num_tickets
            self.passengers_down[train_num - 1] += num_tickets
            self.money_up[train_num - 1] += total_price
            self.money_down[train_num - 1] += total_price

            # Update available seats
            self.available_seats_up[train_num - 1] -= num_tickets
            self.available_seats_down[train_num - 1] -= num_tickets

            print(f'Tickets purchased successfully for Train {train_num}. Total cost: ${total_price}')
        else:
            print(f'Error: Not enough seats available on Train {train_num}.')

    def display_summary(self):
        # Display the number of passengers and money for each train journey
        for i in range(self.num_trains):
            print(f'Train {i + 1} (Up) - Passengers: {self.passengers_up[i]}, Money: ${self.money_up[i]}')
            print(f'Train {i + 1} (Down) - Passengers: {self.passengers_down[i]}, Money: ${self.money_down[i]}')

        # Calculate and display the total number of passengers and money for the day
        total_passengers = sum(self.passengers_up)
        total_money = sum(self.money_up)

        print(f'Total passengers for the day: {total_passengers}')
        print(f'Total money for the day: ${total_money}')

        # Find and display the train journey with the most passengers
        max_passengers_train = self.passengers_up.index(max(self.passengers_up)) + 1
        print(f'Train {max_passengers_train} had the most passengers today.')


# Main program
if __name__ == "__main__":
    railway = MountainRailway()

    # Task 1 - Start of the day
    railway.display_screen()

    # Main loop for ticket sales
    while any(seats > 0 for seats in railway.available_seats_up):
        # Task 2 - Purchasing tickets interactively
        try:
            train_num = int(input("Enter the train number (1-4) or 0 to stop ticket sales: "))
            if train_num == 0:
                break  # Exit the loop if the operator chooses to stop ticket sales
            elif 1 <= train_num <= 4:
                pass  # Continue with ticket sales
            else:
                print("Invalid train number. Please enter a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        while True:
            try:
                num_tickets = int(input("Enter the number of tickets or 0 to stop for this train: "))
                if num_tickets == 0:
                    break  # Move on to the next train if the operator chooses to stop for this train
                elif num_tickets > 0:
                    pass  # Continue with ticket sales for the specified number of tickets
                else:
                    print("Invalid number of tickets. Please enter a number greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            # Task 2 - Purchasing tickets
            railway.purchase_tickets(train_num, num_tickets)

            # Display updated screen
            railway.display_screen()

    # Task 3 - End of the day
    railway.display_summary()


# In[ ]:




