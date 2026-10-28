def calculate_bill(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative values.")
    return price * quantity

def main():
    print("=== Shopping Bill Calculator (Push 1) ===")
    try:
        price = float(input("Enter the item's price ($): "))
        quantity = int(input("Enter the quantity: "))
        total = calculate_bill(price, quantity)
        print(f"\nTotal Amount Due: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
