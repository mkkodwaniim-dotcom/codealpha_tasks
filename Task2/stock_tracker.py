stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

total = 0

while True:
    stock_name = input("Enter stock name (or type done): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock_name] * quantity
        total += investment
        print("Investment value:", investment)
    else:
        print("Stock not found!")

print("Total Investment:", total)

# Save result in file
file = open("portfolio.txt", "w")
file.write("Total Investment = " + str(total))
file.close()

print("Result saved in portfolio.txt")