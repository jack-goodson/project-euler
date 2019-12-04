fib_list = [1,2]
sum = 0

while fib_list[-1] + fib_list[-2] < (4 * 10**6):
    new_entry = fib_list[-1] + fib_list[-2]
    fib_list.append(new_entry)

for n in fib_list:
    if n % 2 == 0:
        sum += n

print(sum)
