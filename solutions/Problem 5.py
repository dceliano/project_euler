high_num = 20 # 1 to high_num
num_worked = 0
smallest_num = 0
test_num = 25 # start at a fairly high number
while(smallest_num == 0):
    test_num += 1
    num_worked = 0
    for i in range(1, high_num + 1):
        if test_num % i == 0: #if we pass the test, increment num_worked
            num_worked += 1
        else:
            break #exit the loop
    if(num_worked == high_num):
        smallest_num = test_num

print(smallest_num)
