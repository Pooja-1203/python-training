def facti(n):
  if n==0 or n==1:
      return 1
      return n*facti(n-1)
print(facti(1))