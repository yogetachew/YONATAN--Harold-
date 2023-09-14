"""
    Filename: yonatans_soccer_ball_shop_main_cli.py
    Author: Yonatan Getachew
    Created: 08/31/23
    Purpose: 
"""
import yonatans_soccer_ball_shop_class as soccerball

def get_input():
        # TODO: Get int input from user
        number_of_soccer_balls = int(input("Enter number of soccer balls: "))
        return number_of_soccer_balls

yonatans_soccerball = soccerball.SoccerballHeaven()

number_of_soccer_ball = get_input()

yonatans_soccerball.calculate()

yonatans_soccerball.display()

