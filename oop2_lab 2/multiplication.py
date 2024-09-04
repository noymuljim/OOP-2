n=5
for i in range(1,11):
    if i==6:
        continue
    if i==9:
        break
    print(f"{n}*{i}= {n*i}")
