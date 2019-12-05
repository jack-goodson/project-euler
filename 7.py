primes = []
n = 2
while len(primes) < 10001:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(n)
    n+=1
print(primes[-1])
