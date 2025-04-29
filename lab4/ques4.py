# Program to calculate the net amount after discount based on toy type and order amount

def calculate_net_amount(product_code, order_amount):
  if product_code == 1:  # Battery Based Toys
    if order_amount > 1000:
      discount = 0.10 * order_amount
    else:
      discount = 0
  elif product_code == 2:  # Key-based Toys
    if order_amount > 100:
      discount = 0.05 * order_amount
    else:
      discount = 0
  elif product_code == 3:  # Electrical Charging Based Toys
    if order_amount > 500:
      discount = 0.10 * order_amount
    else:
      discount = 0
  else:
    print("Invalid product code!")
    return None

  net_amount = order_amount - discount
  return net_amount



product_code = int(input("Enter the product code (1 for Battery Based, 2 for Key-based, 3 for Electrical Charging Based): "))
order_amount = float(input("Enter the order amount: "))
net_amount = calculate_net_amount(product_code, order_amount)
print(f"The net amount to be paid after discount is: Rs. {net_amount:.2f}")
