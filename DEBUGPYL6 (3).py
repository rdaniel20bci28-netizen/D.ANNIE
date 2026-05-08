# add if statement for b = 0 and else for b != 0

a, b = map(int, input().split())
if b==0:
  print("infinity")
else:
  print(a // b)
