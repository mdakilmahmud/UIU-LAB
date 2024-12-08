num = [1,2,3,4,5]
index = 0
even_sum=[]
odd_sum=[]
while index<len(num):
  if index%2==0:
    even_sum.append(index)
  else:
    odd_sum.append(index)
  index+=1
print(sum(even_sum))
print(sum(odd_sum))
