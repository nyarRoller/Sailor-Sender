n = input()

mas = list(map(int, input().split()))

st = 0

suc = False
if mas[0] == mas[-1]:
    st = 1

for element in mas:
    k = st
    for i in range(len(mas)-1):
        if mas[i] == element and mas[i + 1] == element:
            k += 1

        if k == 2:
            suc = True
            break
    if suc:
        break

if suc:
    print("Yes")
else:
    print("No")
