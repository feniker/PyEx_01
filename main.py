n = int(input("n = "))
out = open('output.txt', 'w')
simple = [2]
for i in range(3, n+1, 2):
    if(i % 10 == 5):
        continue
    for j in simple:
        if(j*j > i):
            simple.append(i)
            break
        if i % j == 0:
            break
    else:
        simple.append(i)
print(simple, file = out)
out.close()