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
