num_1 = 1
num_2 = 2 #num_2 will be the newest value
digits = 1000 #number of digits to find
index = 2 #start out at 2
done = 0
while done == 0:
    index += 1
    new_num_1 = num_2
    num_2 += num_1
    num_1 = new_num_1
    if(num_2 / (10**(digits - 1)) >= 1): #if the number is 1,000 digits
        done = 1
print(index + 1)
print(num_2)
