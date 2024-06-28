height = 100.0
bounce_number = 1
while bounce_number <= 10:
    height = round((3 / 5) * height, 4)
    print(bounce_number, height)
    bounce_number += 1