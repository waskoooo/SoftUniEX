start_number = int(input())
if start_number <= 100:
    bonus_point = 5
elif start_number <= 1000:
    bonus_point = start_number * 0.20
else:
    bonus_point = start_number * 0.10
bonus_extra_point = 0
if start_number % 2 == 0:
    bonus_extra_point = 1
if start_number % 10 == 5:
    bonus_extra_point = bonus_extra_point + 2

print(bonus_point + bonus_extra_point)
print(start_number + bonus_point + bonus_extra_point)