#!/usr/bin/env python
# coding: utf-8

# In[25]:


import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length**2

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        print(f"Area of Hexagon is: {self.calcArea()}")
        print(f"Perimeter of Hexagon is: {self.calcPeri()}")
        print(f"Sum of angles of Hexagon is: {self.calcAngleSum()}")

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length**2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print(f"Area of Square is: {self.calcAreaSquare()}")
        print(f"Perimeter of Square is: {self.calcPeriSquare()}")

def main():
    cnic = "1610111068415"
    last_digit = int(cnic[-1])
    hexagon_side = last_digit

    hexagon = Hexagon(hexagon_side)
    square = Square(last_digit + 1)

    while True:
        print("Press 1 to calculate area, perimeter, and sum of angles of hexagon: ")
        print("Press 2 to calculate area and perimeter of square: ")
        print("Press any other key to exit...")

        choice = input()

        if choice == '1':
            hexagon.display()
        elif choice == '2':
            square.display()
        elif choice != '1' and choice !='2':
            print("Exiting program.")
            break
if __name__ == "__main__":
    main()


# In[ ]:




