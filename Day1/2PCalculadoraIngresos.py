myName = input("What is your name: ")
myMoney = int(input("How many money make: "))
myTax = round((myMoney * 21 / 100),2)

print(f"Dear {myName} with your benefits {myMoney} you will pay tax in spain : {myTax} thx")