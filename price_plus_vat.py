try:
    price = float(input("Enter price: "))
    new_price = price + price * 0.24
    print(f"The price with VAT is {new_price:.2f}")
    
except ValueError:
    print("Invalid price")
