par = impar = 0

for n in range(1,101):
  n = int(input())
  if n%2==0:
    par += 1
  if n%2==1:
    impar += 1
    
print(f'{par}/n{impar}')