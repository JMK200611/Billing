def calculate_bill(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    return price * quantity

def calculate_discounted_bill(price, quantity, discount_percent=0):
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percentage must be between 0 and 100")
    total = calculate_bill(price, quantity)
    return total - (total * (discount_percent / 100.0))

def main():
    print("--- Shopping Bill Calculator ---")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        
        # --- PUSH 1 FUNCTIONALITY ---
        total = calculate_bill(price, quantity)
        print(f"Base Total Bill: ${total:.2f}")
        
        # --- PUSH 2 FUNCTIONALITY (Discount Addition) ---
        choice = input("Apply a discount? (y/n): ").strip().lower()
        if choice == 'y':
            discount = float(input("Enter discount percentage (0-100): "))
            final_total = calculate_discounted_bill(price, quantity, discount)
            print(f"Final Discounted Bill: ${final_total:.2f}")
        else:
            print(f"Final Bill: ${total:.2f}")
            
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
