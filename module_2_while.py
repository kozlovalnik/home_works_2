
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
current_value = 0

while current_value < len(my_list):
    if my_list[current_value] >= 0:
        print(my_list[current_value])
        current_value += 1
        continue
    else:
        break
