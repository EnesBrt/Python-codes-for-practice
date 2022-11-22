from art import logo

print(logo)
print("Welcome to : Interenchères !!!!")

user = {}
ask_user = True

while ask_user:
    name = input("What is your name ?\n")
    bid_price = int(input("What is your bid price ?\n"))
    user[name] = bid_price
    ask_auction = input("Other users who want to bid ?\n")

    if ask_auction == "no":
        max_value = max(user, key=user.get)
        print(f"And the winner is... {max_value} !")
        break
    elif ask_auction == "yes":
        continue
    else:
        print("You must answer by yes or no !")
        break



