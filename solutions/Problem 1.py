max_num = 1000
sum = 0
for i in range(1,max_num):
    if (i % 3 == 0) or (i % 5 == 0):
        print(i)
        sum += i
print(sum)
