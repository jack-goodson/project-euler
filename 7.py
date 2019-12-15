#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

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
