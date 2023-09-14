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

def display():
        # TODO: Display transaction for customer
        number_of_soccer_balls = soccerball.SoccerballHeaven.number_of_soccer_balls
        total_sale = soccerball.SoccerballHeaven.total_sale
        print(f"Number of soccer balls: {number_of_soccer_balls}")
        print(f"Your total cost was: ${total_sale:,.2f}")

number_of_soccer_balls = get_input()

yonatans_soccerball = soccerball.SoccerballHeaven()

yonatans_soccerball.calculate(number_of_soccer_balls)

yonatans_soccerball.display()

