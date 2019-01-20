''' Fizz Buzz '''
theLst = []
primes =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
thePrimelst =[]
for num in range(0,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz',num)
        theLst.append(num)
        continue
    if num % 3 == 0:
        print('Fizz',num)
        theLst.append(num)
        continue
    if num % 5 == 0:
        print('Buzz',num)
        theLst.append(num)
print(theLst)
print(primes)

for item in theLst:
    if item in primes:
        print(item)
        thePrimelst.append(item)

print(thePrimelst)