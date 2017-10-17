current_num = 100 #given
my_sum = current_num * (current_num - 1) #number to start out
current_num -= 1
while((current_num-1) != 0):
    current_num -= 1
    my_sum = my_sum * current_num
print(my_sum)
sum_str = str(my_sum)
char_sum = 0
for char in sum_str:
    char_sum += int(char)
print(char_sum)
