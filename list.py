ex1 = list()
ex1 = []

print(type(ex1))


primes = [2,3,5,7,11,13,17,19]

print(primes)

print(primes[2:4])

print(primes[-2:8])

#indexing

print(primes[4])


## multiple data types in the same list

l1 = [12,235,34,'and','letters','numbers']

print(l1)

nums = [1,2,3,4,5,6]

letters = ['a','b','c','d']

print(nums + letters)

l1.reverse()

print(l1)

## Tuples

p1 = ('john','23','rg21 7ts')

print(type(p1))

name = p1[0]
age = p1[1]
postcode = p1[2]

print("Name :", name)

print ("Age :", age)


p2 = ('john','23','rg21 7ts')

name, age, postcode = p2


print("About john:", p2)



