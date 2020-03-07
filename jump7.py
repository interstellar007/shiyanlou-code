for a in range(1,101):
    if a % 7 == 0 or (a - 7) % 10 == 0 or 10 <= a / 7 < 11.4:
        continue
    print(a) 
