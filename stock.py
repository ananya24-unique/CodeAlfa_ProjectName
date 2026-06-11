stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 180,
    "MSFT": 420
}

print("Available stocks: AAPL, TSLA, GOOGL, AMZN, MSFT")
print("Enter 'done' when finished.")

total = 0

while True:
    name = input("\nEnter stock name: ").upper()
    
    if name == "DONE":
        break
    
    if name not in stocks:
        print("Stock not found!")
        continue
    
    quantity = int(input("Enter quantity: "))
    value = stocks[name] * quantity
    print(f"{name} x {quantity} = ${value}")
    total += value

print(f"\nTotal Investment: ${total}")