#Q1
n=5
k=round(n/2)*2
for i in range(0,n,2):
  for j in range(0,k+1):
    print(end='')
  for j in range(0,i+1):
    print('* ',end='')
  k=k-2
  print()
k=1
for i in range(n-1,0,-2):
  for j in range(0,k+2):
    print(end='')
  for j in range(0,i-1):
    print('* ',end='')
  k+=2
  print()

#2
n=5
s=n*2-1
for i in range(1,n+1):
  for j in range(0,s):
    print(end='')
  for j in range(i,0,-1):
    print(j,end='')
  s-=2
  print()

#3
n=5
s=0
for i in range(n-1,0,-1):
  for j in range(0,s+1):
    print(end='')
  for j in range(1,i+1):
    print(j,end='')
  s+=2
  print()

#4
n=3
j=n-1
print(' '*n+'*')
for i in range(1,2*n):
  if i>n:
    print(' '*(i-n)+'*'+' '*(2*j-1)+'*')
    j-=1
  else:
    print(' '*(n-i)+'*'+' '*(2*i-1)+'*')
if n>i:
  print(' '*n+'*')

#5
n=3
for i in range(1,n+1):
  print(' '*(n-i)+'*'*(2*i-1))
for i in range(n-1,0,-1):
  print(' '*(n-i)+'*'*(2*i-1))

#6
n=4
for i in range(1,n+1):
  if i==1:
    print('* ')
  else:
    print('* '+' '*(i-2)+'*')
for i in range(n-1,0,-1):
  if i==1:
    print('* ')
  else:
    print('* '+' '*(i-2)+'* ')

#7
for i in range(1,8):
  x=65
  for j in range(1,i+1):
    print(chr(x),end=' ')
    x+=1
  print()

#8
for i in range(65,70):
  for j in range(65,i+1):
    print(chr(i),end=' ')
  print()

#9
for i in range(2,9,2):
    for j in range(2,i+1,2):
        print(i,end=' ')
    print()
