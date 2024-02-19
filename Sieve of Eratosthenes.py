#Sieve of Eratosthenes
#The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).

#finds all the prime numbers less than or equal to a given integer n by Eratosthenes' method:
def sieve(n):
    nums = list(range(2,n+1))
    print(nums)
    i = 0
    while nums[i]**2 <= n:
        #loop thorugh it's multiple, then add one to index
        j = nums[i]
        while nums[i]*j <= n and nums[i] :
            try:
                nums.remove(nums[i]*j)
            except:
                pass
            j += 1
        i += 1
    return(nums)
   
print(sieve(30))


#alternativeley:


def SieveOfEratosthenes(n):
    nums = [True for i in range(n+1)]
    i = 2
    while i**2 <= n:
        j = i**2
        if nums[i]:
            while j <= n:
                nums[j] = False
                j += i
        i += 1
    for i in range(2,n+1):
        if nums[i]:
            print(i)


print(SieveOfEratosthenes(30))
