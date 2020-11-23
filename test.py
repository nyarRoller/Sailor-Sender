m = int(input())
mi = list(map(int,input().split()))
ci = list(map(int,input().split()))

miNew = mi
ciNew = ci

answer = []
run = True
mas = 0

while run:
    n = ciNew.index(max(ciNew))
    value = max(ciNew)
    print(value,n)
    if mas + miNew[n]  <= m:
        mas += miNew[n]
        answer.append(mi.index(miNew[n])+1)xD
        miNew.pop(n)
        ciNew.pop(n) 
        print("succsesful", value)
        print("mi : ",mi)
        print("miNew : ", miNew)
    else:
        miNew.pop(n)
        ciNew.pop(n)
    if len(miNew) == 0 or len(ciNew) == 0:
        run = False 
print(answer)