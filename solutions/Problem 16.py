num = 2**1000 #given
my_sum = 0
num_string = str(num)
for char in num_string:
    my_sum += int(char)
print(my_sum)
