def apply_discount(price, discount_percentage):
    """Məhsulun qiymətinə endirim tətbiq edir."""
    # Endirim məbləğini faizlə hesablayırıq
    discount_amount = price * discount_percentage / 100
    
    # DÜZƏLİŞ: Endirim faizini deyil, hesablanmış endirim məbləğini çıxırıq
    final_price = price - discount_amount 
    return final_price

def process_checkout(cart_items):
    print("--- Shopping Cart Checkout ---")
    total_bill = 0
    for item, price in cart_items.items():
        # Hər məhsula 10% endirim
        discounted = apply_discount(price, 10)
        print(f"Item: {item} | Original: ${price} | Final: ${discounted}")
        total_bill += discounted
    
    print(f"\nGrand Total to Pay: ${total_bill}")

# Test məlumatları
my_cart = {
    "Laptop": 1200,
    "Mouse": 50,
    "Keyboard": 100
}

process_checkout(my_cart)
