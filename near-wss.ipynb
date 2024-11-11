# importing library
import math

# prime number test
def isPrime(n):
  if n==2 or n==3:
    return True
  else:
    for i in range(2, math.ceil(math.sqrt(n))+1):
      if n%i==0:
        return False
      elif i==(math.ceil(math.sqrt(n))):
        return True
      else:
        continue

# number of prime number
def pi(n):
  count = 0
  for i in range(1, n+1):
    if isPrime(i)==True:
      count = count+1
  return count

# Legendre symbol where p=5
def legendre(n):
  if n%5==1 or n%5==4:
    return 1
  elif n%5==2 or n%5==3:
    return -1
  else:
    return 0

# Fibonacci number
f = [0,1]

for i in range(2, 512000): # 512000 근방이 RAM 한계인 것으로 추정됨
  f.append(f[i-1]+f[i-2])

# Wall-Sun-Sun prime
def wss(i):
  return f[i-legendre(i)]%(i**2)

# near WSS
def nearWSS(i, k):
  global cnt
  cnt = 0
  temp = wss(i) / i
  if temp <= k:
    cnt = 1
    return True
  elif i-k <= temp:
    cnt = -1
    return True
  else:
    return False

# near WSS test
for i in range(2, 512000):
  if isPrime(i) and nearWSS(i, 14.9):
    if cnt == 1:
      print("NW(%d) = %d"%(i, wss(i)/i))
    elif cnt == -1:
      print("NW(%d) = %d"%(i, wss(i)/i-i))
