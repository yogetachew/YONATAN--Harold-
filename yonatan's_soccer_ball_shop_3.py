"""
    Filename: yonatan's_soccer_ball_shop_3.py
    Author: Yonatan Getachew
    Created: 08/31/23
    Purpose: 
"""

# Cost of soccer ball for the custumer
SOCCER_BALL_COST = 7.95

class SoccerballHeaven:
    def __init__(self):
        pass

    def get_input(self):
        # TODO: Get int input from user
        self.number_of_soccer_balls = int(input("Enter number of soccer balls: "))

    def calculate(self):
        # TODO: calculate costs of the hotdogs purchased
        self.total_sale = self.number_of_soccer_balls * SOCCER_BALL_COST
        

    def display(self):
        # TODO: Display transaction for customer
        print(f"Your total cost was: ${self.total_sale:,.2f}")

yonatans_soccerball = SoccerballHeaven()
yonatans_soccerball.get_input()
yonatans_soccerball.calculate()
yonatans_soccerball.display()