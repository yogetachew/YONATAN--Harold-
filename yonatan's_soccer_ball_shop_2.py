"""
    Filename: yonatan's_soccer_ball_shop_2.py
    Author: Yonatan Getachew
    Created: 08/31/23
    Purpose: functional POS program
"""

# Cost of soccer ball for the custumer
SOCCER_BALL_COST = 4.95

def main():
    num_of_soccer_balls = get_input()
    total_sale = calculate(num_of_soccer_balls)
    display(total_sale)

def get_input():
    # TODO: Get int input from user how many soccer balls sold
    number_of_soccer_balls = int(input("Enter number of soccer balls: "))
    return number_of_soccer_balls

def calculate(number_of_soccer_balls):
    # TODO: calculate costs of the hotdogs purchased
    total_sale = number_of_soccer_balls * SOCCER_BALL_COST
    return total_sale

def display(total_sale):
    # TODO: Display transaction for customer
    print(f"Your total cost was: ${total_sale:,.2f}")

if __name__ == '__main__':
    main()