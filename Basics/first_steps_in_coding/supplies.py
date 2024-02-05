pen_packet = 5.80
marker_packet = 7.20
washing_liquid = 1.20

pen_count = int(input())
count_marker = int(input())
count_washing_liq = float(input())
discount = int(input()) / 100

pen_cost = pen_packet * pen_count
market_cost = marker_packet * count_marker
cost_washing = washing_liquid * count_washing_liq

all_materials = pen_cost + market_cost + cost_washing
discount_proc = all_materials * discount

final_cost = all_materials - discount_proc

print(final_cost)




