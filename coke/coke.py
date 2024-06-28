print("Amount Due: 50")
paid = 0

while paid < 50:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        paid = paid + coin
        if paid < 50:
            print("Amount Due:", 50 - paid)
    else:
        print("Amount Due:", 50 - paid)

print("Change Owed:", paid - 50)

