my_list = [10,20,35,30,40]
sum=0
for i in my_list:
  if i%5==0 and i%10==0:
    sum=sum+i
print(sum)