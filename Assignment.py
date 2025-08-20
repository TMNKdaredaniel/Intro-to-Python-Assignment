# creating function
# defining function
def calculate_discount(price, discount_percent):
    # local variable
    # final_price
    if discount_percent >= 20:
        discount_percent = discount_percent / 100
        discount = discount_percent * price
        final_price = price - discount
        print(f'The discount is {discount_percent}%, and the final price is ${final_price}.')
    else:
        print(f"The percentage {discount_percent}% is too low,  ${price} is the original price. That is all!")

# Prompting user to enter the orriginal price and discount percentage
price = float(input("Enter the price: "))
discount_percent = int(input("Enter the percentage: "))

# Using calculate_discount Function
calculate_discount(price, discount_percent) 


            