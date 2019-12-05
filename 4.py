large_palin = 0
for first in range(1, 1000):
    for second in range(1, 1000):
        num = first * second
        s_num = str(num)
        s_num1 = s_num[:len(s_num)//2]
        s_num2 = s_num[len(s_num) // 2:][::-1]
        if s_num1 == s_num2 and num > int(large_palin):
            large_palin = s_num

print(large_palin)
