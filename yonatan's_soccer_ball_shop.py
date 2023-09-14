"""
    Filename: yonatan's_soccer_ball_shop.py
    Author: Yonatan Getachew
    Created: 08/31/23
    Purpose: 
"""

# Cost of soccer ball for the custumer
SOCCER_BALL_COST = 4.95

# TODO: Get int input from user
number_of_soccer_balls = int(input("Enter number of soccer balls: "))

# TODO: calculate costs of the hotdogs purchased
total_receipt = number_of_soccer_balls * SOCCER_BALL_COST

# TODO: Display transaction for customer
print(f"Your total cost was: ${total_receipt:,.2f}")