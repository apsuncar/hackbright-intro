primes = [1,3]
# primes + 5
primes = primes + [5]
print primes 
primes.append(7)
primes.append(11)
print primes
primes.append([7,11])
print primes

primes.pop()
print primes 

# primes.extend(13,17)
# print primes 

primes.extend([13,17])
print primes 