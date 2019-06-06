def int_rev(num):
  rev = 0
  while(num > 0):
    a = num % 10
    rev = (rev * 10) + a
    num = num // 10
  return(rev)

# Driver Function 
num = [256]
