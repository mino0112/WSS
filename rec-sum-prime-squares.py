sum = 0

def is_prime(x):
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return 0
  return 1

for i in range(2, 10**7):
  if is_prime(i):
    sum += 1 / (i**2)

print(sum)
