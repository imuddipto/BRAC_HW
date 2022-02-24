n = int(input())

while(n>0):
  j=n
  print(" "* (5-n), end="")
  while (j > 0):
    print(j, end="")
    j -=1
  print()
  n -= 1
