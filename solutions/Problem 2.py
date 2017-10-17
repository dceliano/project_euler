num_1 = 1
num_2 = 2 #num_2 will be the newest value
sum = 2 #start out at 2 since we're not including it
while num_2 <= 4000000:
    new_num_1 = num_2
    num_2 += num_1
    num_1 = new_num_1
    if(num_2 % 2 == 0): #if even
        sum += num_2
    print(num_2)
print(sum)
