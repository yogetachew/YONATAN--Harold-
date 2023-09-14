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

    def get_number_soccerballs(self):
        # validation
        if self._number_of_soccer_balls > 0:
            return self._number_of_soccer_balls
        else:
            return "You must order at least on soccer ball"
    def get_total_sale(self):
        return self._total_sale

    def calculate(self, number_of_soccer_balls):
        # TODO: calculate costs of the hotdogs purchased
        self._number_of_soccer_balls = number_of_soccer_balls
        self._total_sale = self._number_of_soccer_balls * SOCCER_BALL_COST
        
