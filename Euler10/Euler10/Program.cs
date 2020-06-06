using System;

namespace Euler10
{
    internal class Program
    {
        public static void Main()
        {
            
            long primeProduct = 0;
            long prime = 2;
            
            while (prime < 2000000)
            {
                if (isPrime(prime))
                {
                    primeProduct += prime;
                }

                prime++;
            }

            Console.Write(primeProduct);
        }
        
        private static bool isPrime(long n)
        {
            if (n <= 3)
            {
                return n > 1;
            }else if (((n % 2) == 0) || ((n % 3) == 0))
            {
                return false;
            }
            int i = 5;
            while ((i * i) <= n)
            {
                if (((n % i) == 0) || ((n % (i+2)) == 0))
                {
                    return false;
                }
                i += 6;
            }
            return true;
        }
    }
}