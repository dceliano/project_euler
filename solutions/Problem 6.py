sum_squares = 0
sum = 0
for i in range(1,101):
    sum += i
    sum_squares += (i*i)
sum_squared = (sum*sum)
diff = sum_squared - sum_squares
print(diff)
