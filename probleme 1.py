L=0
R=0
Q=0
for i in range(3):
 print("Enter the name and surname of client",i+1,":")
 p = input()
 print("Enter the number of items for client",i+1,":")
 a = int(input())
 for j in range(0,a):
  print("Enter the price of item",j+1,":")
  s=float(input())
  if i == 0 :
      x = p
      v = s+s*0.15-s*0.02
      L += v
  if i == 1 :
      y = p
      g = s+s*0.15-s*0.02
      R += g
  if i == 2 :
      u = p
      f = s+s*0.15-s*0.02
      Q += f
print("The total price for client",x,"is :",L,"DH")
print("The total price for client",y,"is :",R,"DH")
print("The total price for client",u,"is :",Q,"DH")
