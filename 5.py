#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

small_divis = 0
n = 1
while small_divis == 0:
    tester = True
    for x in range(1,21):
        if n % x != 0:
            tester = False
    if tester == True:
        print(n)
        break
    n += 1
