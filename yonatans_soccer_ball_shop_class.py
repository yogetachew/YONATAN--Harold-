"""
    Filename: yonatans_soccer_ball_shop_class.py
    Author: Yonatan Getachew
    Created: 08/31/23
    Purpose: 
"""

# Cost of soccer ball for the custumer
SOCCER_BALL_COST = 7.95

class SoccerballHeaven:
    def __init__(self):
        pass

    def calculate(self, number_of_soccer_balls):
        # TODO: calculate costs of the hotdogs purchased
        self.number_of_soccer_balls = number_of_soccer_balls
        self.total_sale = self.number_of_soccer_balls * SOCCER_BALL_COST
        

    def display(self):
        # TODO: Display transaction for customer
        print(f"Number of soccer balls: {self.number_of_soccer_balls}")
        print(f"Your total cost was: ${self.total_sale:,.2f}")