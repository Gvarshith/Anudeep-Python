distance = int(input("Enter distance in km: "))
def price(distance):
    if distance <= 50:
      return 8 * distance
    elif distance <= 100:
      return 10 * distance
    else:
      return 12 * distance
print("cost of your journey is ", price(distance),"Rs")