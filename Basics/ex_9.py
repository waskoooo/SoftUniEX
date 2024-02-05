greening_price = 7.61

area_for_greening = float(input())

area_price = greening_price * area_for_greening

discount = area_price * 0.18

final_cost = area_price - discount

print(f"The final price is: {final_cost} lv.")
print(f"The discount is: {discount} lv.")
