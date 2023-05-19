# product details
Products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": {"threshold": 200, "amount": 10},
    "bulk_5_discount": {"threshold": 10, "percentage": 5},
    "bulk_10_discount": {"threshold": 20, "percentage": 10},
    "tiered_50_discount": {"threshold_total": 30, "threshold_single": 15, "percentage": 50}
}



gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10
quantities = {}
gift_wrap_totals = {}
subtotal = 0
discount_name = ""
discount_amount = 0




# User input
for product_name, price in Products.items():
    quantity = int(input(f"Enter the quantity for {product_name}: "))
    quantities[product_name] = quantity

    is_gift_wrapped = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"
    gift_wrap_totals[product_name] = gift_wrap_fee * quantity if is_gift_wrapped else 0

    subtotal += price * quantity




# beneficial discount
for rule, rule_details in discount_rules.items():
    if rule == "flat_10_discount" and subtotal > rule_details["threshold"]:
        discount_name = rule
        discount_amount = rule_details["amount"]
    elif rule == "bulk_5_discount":
        max_quantity = max(quantities.values())
        if max_quantity > rule_details["threshold"]:
            discount_name = rule
            discount_amount = (max_quantity * Products[product_name]) * (rule_details["percentage"] / 100)
    elif rule == "bulk_10_discount" and sum(quantities.values()) > rule_details["threshold"]:
        discount_name = rule
        discount_amount = subtotal * (rule_details["percentage"] / 100)
    elif rule == "tiered_50_discount" and sum(quantities.values()) > rule_details["threshold_total"]:
        max_quantity = max(quantities.values())
        if max_quantity > rule_details["threshold_single"]:
            discount_name = rule
            discount_amount = (max_quantity - rule_details["threshold_single"]) * Products[product_name] * (
                    rule_details["percentage"] / 100)



# shipping fee
shipping_fee = (sum(quantities.values()) // units_per_package) * shipping_fee_per_package



# total
total = subtotal - discount_amount + shipping_fee + sum(gift_wrap_totals.values())




print("----- Purchase Details -----")
for product_name, quantity in quantities.items():
    product_total = Products[product_name] * quantity
    print(f"{product_name}: Quantity: {quantity}, Total: {product_total}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_name} (-${discount_amount})")
print(f"Shipping Fee: {shipping_fee}")
print(f"Total: {total}")
